---
type: rust-concept
topic: generics-traits
level: core
tags:
  - rust
  - generics
  - traits
---

# 泛型与 Trait

## 要解决的问题

泛型让同一段逻辑适用于多种类型；Trait 则描述类型必须提供的行为。二者组合后，可以在不牺牲静态检查和性能的前提下复用代码。

## 泛型函数与 trait bound

```rust
fn larger<T: Ord>(left: T, right: T) -> T {
    if left >= right {
        left
    } else {
        right
    }
}

println!("{}", larger(3, 7));
println!("{}", larger("rust", "go"));
```

`T: Ord` 是 trait bound，表示 `T` 必须实现全序比较。没有这个约束，编译器无法保证 `>=` 对所有 `T` 都存在。

同样的约束也可以写成 `where`：

```rust
fn larger<T>(left: T, right: T) -> T
where
    T: Ord,
{
    if left >= right { left } else { right }
}
```

复杂约束使用 `where` 通常更易读。

## 自定义 Trait

```rust
trait Summary {
    fn summary(&self) -> String;
}

struct Article {
    title: String,
}

impl Summary for Article {
    fn summary(&self) -> String {
        format!("article: {}", self.title)
    }
}
```

Trait 描述“能做什么”，而 struct/enum 描述“保存什么数据”。一个类型可以实现多个 trait，一个 trait 也可以被多个类型实现。

### 默认实现与约束

```rust
trait Label {
    fn label(&self) -> String {
        String::from("unnamed")
    }
}

fn print_label<T: Label>(value: &T) {
    println!("{}", value.label());
}
```

默认实现可以被具体类型覆盖。泛型函数通过 `T: Label` 获得调用 `label` 的权限。

## `impl Trait`

参数位置的 `impl Trait` 是泛型 bound 的简写：

```rust
fn print_summary(value: &impl Summary) {
    println!("{}", value.summary());
}
```

返回位置的 `impl Trait` 表示返回某个确定但不公开具体类型的值：

```rust
fn make_numbers() -> impl Iterator<Item = i32> {
    1..=3
}
```

返回位置的 `impl Trait` 只能代表一个具体类型，不能在不同分支返回两个不同的实现类型。需要运行时选择时，才考虑 trait object，例如 `Box<dyn Summary>`。

## 关联类型

Trait 可以声明关联类型，让实现者为它指定一个相关类型：

```rust
trait Container {
    type Item;

    fn get(&self) -> Option<&Self::Item>;
}
```

标准库的 `Iterator` 使用 `type Item` 表示每次迭代产生的类型。关联类型适合表达“一个实现对应一种固定输出类型”的关系。

## 静态与动态分发

- 泛型和 `impl Trait` 通常使用单态化，在编译期为具体类型生成代码。
- `dyn Trait` 使用动态分发，通过 vtable 在运行时选择实现。

默认优先使用泛型和静态分发；只有确实需要异构集合、运行时替换实现或隐藏具体类型时，再使用 trait object。

## 常见误区

- 忘记为泛型操作添加所需 trait bound。
- 把 `impl Trait` 当作可以返回多个不同具体类型的联合类型。
- 过早使用 `dyn Trait`，导致所有权和生命周期更复杂。
- 在外部类型上实现外部 trait，触发孤儿规则（orphan rule）。
- Trait 只声明行为，不会自动给类型增加字段。

## 自测

1. 为什么 `larger<T>` 必须要求 `T: Ord`？
2. 参数位置 `impl Trait` 和显式泛型有什么主要区别？
3. 什么时候选择关联类型，什么时候选择额外的泛型参数？
4. 为什么 `impl Iterator` 返回值不能在不同分支返回不同迭代器类型？

## 延伸

- [[Rust学习/03-标准库与工程/迭代器与闭包|迭代器与闭包]]
- [[Rust学习/02-类型系统/Option-Result-错误传播|Option、Result 与错误传播]]
- blanket implementation、孤儿规则与 trait coherence
