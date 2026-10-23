---
type: rust-concept
topic: const-static-macros
level: core
tags:
  - rust
  - const
  - static
  - macros
  - compile-time
---

# `const`、`static` 与宏

## 要解决的问题

Rust 中有几种看起来都像“提前写好一段东西”的机制：

- `const`：编译期可求值的命名值。
- `static`：程序整个运行期间存在的单一存储位置。
- `const fn`：可以参与编译期求值的函数。
- `foo!(...)`：宏调用，展开为另一段 Rust 语法。
- `#[...]`：属性语法，给项目附加编译器指令，或调用属性/派生宏变换项目。

它们解决的问题不同。优先选择类型系统和普通函数；只有确实需要共享地址、编译期求值或语法生成时，才使用 `static` 或宏。

## 一页比较

| 机制 | 本质 | 主要时间点 | 是否有单一地址 | 适合场景 |
| --- | --- | --- | --- | --- |
| `const` | 编译期可求值的命名值 | 使用处被求值/替换 | 不保证 | 数字、字符串字面量、数组长度、配置边界 |
| `static` | 一份全局存储 | 运行期间一直存在 | 是 | 只读全局数据、原子计数器、全局初始化状态 |
| `const fn` | 可参与 const-eval 的函数 | 调用处可能在编译期求值 | 取决于返回值 | 用类型安全的函数计算常量 |
| `macro_rules!` | token 模式匹配与展开 | 编译期展开 | 不适用 | 重复语法、可变数量参数、生成声明 |
| 函数式宏 `foo!(...)` | 声明宏或过程宏的调用 | 编译期展开 | 不适用 | 输入不是普通表达式，或需要自定义语法 |
| `#[derive(...)]` | 派生宏/编译器派生机制 | 编译期生成 `impl` | 不适用 | 为 struct/enum 生成 trait 实现 |
| `#[attr]` | 属性或属性过程宏 | 编译期处理项目 | 不适用 | 条件编译、诊断、框架入口、变换函数/模块 |

## `const`：编译期值

```rust
const MAX_RETRIES: usize = 3;
const BUFFER_SIZE: usize = 1024;
const GREETING: &str = "hello";

fn retry_limit() -> usize {
    MAX_RETRIES
}
```

`const` 的初始化表达式必须能通过 const evaluation。它适合表达“值是什么”，而不是表达“所有代码都共享哪个地址”。

### `const` 的关键性质

- 不能被修改。
- 每个使用处可以独立求值或内联，不承诺所有使用处指向同一地址。
- 需要显式类型时，类型检查和普通值一样进行。
- 可以用于数组长度、常量泛型参数和 `match` 模式等需要编译期值的地方。
- 普通运行时操作、I/O 和许多堆分配操作不能放进常量初始化；例如普通 `String::from` 不是常量初始化的通用替代品。

如果只是想给一个固定阈值命名，优先使用 `const`：

```rust
const MAX_ITEMS: usize = 10;

fn accepts(items: &[u8]) -> bool {
    items.len() <= MAX_ITEMS
}
```

## `static`：单一存储位置

```rust
static APP_NAME: &str = "study-notes";

fn app_name_address() -> *const u8 {
    APP_NAME.as_ptr()
}
```

一个 `static` 在整个程序运行期间存在，并代表一个固定的存储位置。它适合“全局只有这一份状态”的场景，而不是普通常量的替代写法。

### 只读 `static`

只读 `static` 仍然要求其类型满足适合全局共享的约束，通常会使用 `Sync` 类型：

```rust
use std::sync::atomic::{AtomicUsize, Ordering};

static REQUESTS: AtomicUsize = AtomicUsize::new(0);

fn record_request() {
    REQUESTS.fetch_add(1, Ordering::Relaxed);
}

fn request_count() -> usize {
    REQUESTS.load(Ordering::Relaxed)
}
```

这里需要 `static` 是因为原子计数器必须被所有调用者共享同一份状态；如果写成 `const`，每个使用处都只会得到一个独立的值，无法实现计数。

### 不要把 `static mut` 当作普通全局变量

```rust
// 不推荐：读写 static mut 需要 unsafe，并且容易产生数据竞争。
static mut LEGACY_COUNT: usize = 0;
```

`static mut` 的读写涉及 `unsafe`，多线程下还需要额外同步。新代码通常使用 `Atomic*`、`Mutex`、`RwLock`、`OnceLock` 或 `LazyLock` 等安全抽象：

```rust
use std::sync::{Mutex, OnceLock};

static CONFIG: OnceLock<Mutex<Vec<String>>> = OnceLock::new();

fn config() -> &'static Mutex<Vec<String>> {
    CONFIG.get_or_init(|| Mutex::new(Vec::new()))
}
```

### `const` 与 `static` 的选择

- “这是一个固定值”：用 `const`。
- “程序里只有一份、需要共享地址或可变状态”：用 `static`。
- “需要延迟初始化”：优先用 `OnceLock`/`LazyLock`，而不是手写 `static mut`。
- “需要共享可变状态”：把同步原语放进 `static`，不要裸露无保护的全局可变内存。

### 不要混淆 `static` 与 `'static`

- `static` 是声明项目和存储位置的关键字，例如 `static REQUESTS: AtomicUsize`。
- `'static` 是生命周期或 trait bound，表示引用能持续到程序结束，或某个类型不包含短生命周期借用。
- 一个拥有数据的值也可以满足 `T: 'static`，例如 `String`；这不表示这个 `String` 永远不会被释放，只表示它不借用一个更短生命周期的数据。

```rust
fn accepts_owned<T: 'static>(value: T) {
    drop(value);
}

accepts_owned(String::from("owned")); // String 不借用外部数据
```

## `const fn`：用函数计算常量

```rust
const fn square(value: usize) -> usize {
    value * value
}

const LIMIT: usize = square(8);

fn runtime_square(value: usize) -> usize {
    square(value)
}
```

`const fn` 仍然是普通函数，可以在运行时调用；当参数和上下文允许时，也可以在编译期求值。它比宏更有类型检查、作用域和调试体验：

- 能表达普通参数和返回值类型。
- 不需要 token 拼接。
- 不能执行任意运行时副作用。
- 适合纯计算和数组/配置相关的编译期计算。

如果需求只是“根据输入做类型安全的计算”，先考虑 `const fn` 或普通函数，不要先写宏。

## `foo!(...)`：宏调用

感叹号表示这里调用的是宏，而不是普通函数：

```rust
let values = vec![1, 2, 3];
println!("values = {values:?}");
let message = format!("count = {}", values.len());
```

常见宏包括：

- `vec!`：根据元素和重复语法生成 `Vec`。
- `println!`、`format!`：处理格式字符串和可变数量参数。
- `matches!`：把模式匹配压缩成布尔表达式。
- `dbg!`、`panic!`：生成带上下文的调试或终止代码。
- `include_str!`、`env!`、`line!`：在编译期间读取资源或环境信息。

### 宏展开不等于结果在编译期执行

宏本身在编译期展开：

```rust
let message = format!("time: {:?}", std::time::SystemTime::now());
```

`format!` 的语法会在编译期检查并展开，但读取当前时间和分配字符串仍然发生在程序运行时。应区分：

1. **展开时间**：宏把输入 token 变成另一段代码的时间。
2. **执行时间**：展开后的代码真正运行的时间。
3. **求值时间**：某些 `const` 表达式能在编译期计算，但不代表所有宏都能做到。

## `macro_rules!`：声明宏

声明宏用模式匹配 token，并生成 Rust 代码：

```rust
macro_rules! count_items {
    ($($item:expr),* $(,)?) => {
        <[()]>::len(&[$(count_items!(@unit $item)),*])
    };
    (@unit $item:expr) => {
        ()
    };
}

let count = count_items!(10, 20, 30);
assert_eq!(count, 3);
```

它擅长：

- 可变数量参数；
- 重复生成相似语法；
- 根据调用处的语法形状选择展开分支；
- 生成声明、表达式或模式。

它不擅长：

- 检查传入表达式的实际类型；
- 读取运行时值并据此决定展开结果；
- 替代一个简单、类型安全的函数。

声明宏具有宏卫生性（hygiene）：宏内部的局部变量通常不会意外捕获调用处同名变量。宏设计仍要保持展开结果简洁，否则编译器错误会变得难读。

## `#[...]`：属性语法与属性宏

`#[...]` 不是一种单独的“值宏”，而是一类附着在项目上的属性语法：

```rust
#[derive(Debug, Clone)]
struct User {
    name: String,
}

#[test]
fn user_name_is_stable() {
    let user = User {
        name: String::from("Ada"),
    };
    assert_eq!(user.name, "Ada");
}
```

### 常见属性类别

| 形式 | 作用 | 例子 |
| --- | --- | --- |
| 编译器内建属性 | 指示编译器如何处理项目 | `#[cfg]`、`#[allow]`、`#[inline]`、`#[must_use]` |
| 派生宏 | 根据 struct/enum 自动生成 trait 实现 | `#[derive(Debug, Clone)]` |
| 属性过程宏 | 读取并改写整个函数、模块或其他项目 | `#[tokio::main]`、`#[tracing::instrument]` |
| 派生宏生成的辅助属性 | 给派生宏提供额外配置 | `#[serde(rename = "...")]` |

并不是所有 `#[...]` 都会生成一段可见的 Rust 函数；有些只是改变条件编译、诊断或优化提示。

### `#[cfg]` 与 `cfg!` 的区别

```rust
#[cfg(feature = "fast")]
fn mode() -> &'static str {
    "fast"
}

#[cfg(not(feature = "fast"))]
fn mode() -> &'static str {
    "portable"
}
```

`#[cfg(...)]` 会在编译阶段保留或移除项目；被移除的分支不参与后续类型检查。

```rust
let enabled = cfg!(feature = "fast");
```

`cfg!(...)` 只是展开为一个 `bool` 表达式，两个运行时分支都仍然需要通过解析和类型检查。需要“不要编译某段代码”时用 `#[cfg]`，需要“得到一个配置布尔值”时才用 `cfg!`。

## 派生宏、属性宏和函数式过程宏

过程宏通常位于单独的 `proc-macro` crate，接收 `TokenStream` 并生成新的 token：

- **派生宏**：`#[derive(MyTrait)]`，目标是 struct 或 enum，通常生成 trait 实现。
- **属性宏**：`#[route("/users")] fn handler() {}`，可以改写整个函数、模块或项目。
- **函数式过程宏**：`sql!("SELECT ...")` 或 `html! { ... }`，调用形式看起来像 `foo!(...)`，但由过程宏解析自定义输入。

选择顺序通常是：

1. 普通函数或 `const fn`；
2. 泛型、Trait 或 `impl Trait`；
3. `macro_rules!`；
4. 只有需要自定义语法、跨项目生成代码或改写项目时，才引入过程宏。

过程宏能力强，但会增加编译时间、错误定位成本和 crate 结构复杂度。

## 什么时候该用什么

### 用 `const`

- 一个固定值需要名字；
- 需要数组长度、常量泛型或模式中的编译期值；
- 不需要共享地址和可变状态。

### 用 `static`

- 程序必须共享同一份全局存储；
- 需要原子计数器、只读全局数据或一次初始化状态；
- 能用安全同步原语封装共享可变状态。

### 用普通函数或 `const fn`

- 输入和输出类型明确；
- 需求是计算或行为，不是生成语法；
- 希望获得最好的类型检查、文档和调试体验。

### 用 `macro_rules!`

- 参数数量或语法形状需要变化；
- 需要重复生成声明或表达式；
- 普通函数无法表达调用语法。

### 用 `#[...]`

- 需要条件编译、诊断、优化提示或测试标记；
- 需要通过 `derive` 自动生成 trait 实现；
- 使用框架提供的属性宏来注册或改写项目。

## 常见误区

- 用 `static` 代替所有 `const`，误以为“全局值”总是更好。
- 把 `static mut` 当作简单全局变量，忽略数据竞争和 `unsafe`。
- 认为宏展开后就一定是编译期计算结果。
- 用宏实现本来可以用普通函数或 `const fn` 表达的逻辑。
- 把 `#[cfg]` 和 `cfg!` 混用，导致本应被移除的代码仍需通过类型检查。
- 认为所有 `#[...]` 都是过程宏；很多属性是编译器内建指令。
- 用 `macro_rules!` 期待它知道表达式的运行时类型。
- 过程宏生成了大量隐藏代码，却没有提供可读的错误信息或文档。

## 自测

1. 为什么 `const` 不能替代原子计数器的 `static`？
2. `const fn` 和 `macro_rules!` 分别解决哪类问题？
3. 宏展开、编译期求值和运行时执行有什么区别？
4. `#[cfg]` 和 `cfg!` 什么时候分别使用？
5. `#[derive(Debug)]`、属性过程宏和 `foo!(...)` 的输入项目有什么不同？
6. 遇到一个“想少写几行代码”的需求时，为什么不应该马上写宏？

## 延伸

- [[Rust学习/02-类型系统/泛型与Trait|泛型与 Trait]]
- [[Rust学习/03-标准库与工程/迭代器与闭包|迭代器与闭包]]
- `OnceLock`、`LazyLock` 与线程安全的全局初始化
- 声明宏的片段说明符、宏卫生性和递归展开
- `proc-macro` crate、`syn`、`quote` 与过程宏测试
