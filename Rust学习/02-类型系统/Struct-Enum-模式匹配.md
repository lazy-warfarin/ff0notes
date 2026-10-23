---
type: rust-concept
topic: structs-enums-pattern-matching
level: core
tags:
  - rust
  - types
  - pattern-matching
---

# Struct、Enum 与模式匹配

## 要解决的问题

Rust 不依赖继承层次表达所有数据关系，而是通过组合：

- `struct` 表示“多个字段同时存在”的数据。
- `enum` 表示“多个状态中恰好一个成立”。
- `match` 和模式匹配负责安全地拆解这些状态。

`Option` 和 `Result` 也是 enum；先掌握这里的建模方式，再看 [[Rust学习/02-类型系统/Option-Result-错误传播|Option、Result 与错误传播]] 会更自然。

## Struct：组合字段

```rust
struct User {
    name: String,
    active: bool,
}

impl User {
    fn new(name: impl Into<String>) -> Self {
        Self {
            name: name.into(),
            active: true,
        }
    }

    fn deactivate(&mut self) {
        self.active = false;
    }
}

let mut user = User::new("Ada");
user.deactivate();
println!("{}: {}", user.name, user.active);
```

`impl` 中可以定义两类函数：

- 关联函数：没有 `self`，通过 `User::new(...)` 调用，常用作构造器。
- 方法：带 `self`、`&self` 或 `&mut self`，通过实例调用。

### 其他 Struct 形式

```rust
struct Point(i32, i32); // tuple struct
struct Marker;          // unit-like struct

let origin = Point(0, 0);
let _marker = Marker;
```

## Enum：表达互斥状态

```rust
enum Command {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
}
```

一个 `Command` 同时只能处于其中一个变体。每个变体可以携带不同形状的数据，这比给所有字段加一个“类型”字段更直接。

## match：穷尽处理状态

```rust
fn describe(command: Command) -> String {
    match command {
        Command::Quit => String::from("quit"),
        Command::Move { x, y } => format!("move to ({x}, {y})"),
        Command::Write(text) => format!("write: {text}"),
    }
}
```

`match` 必须覆盖所有可能的变体。编译器因此能在新增 enum 变体时提醒所有需要更新的代码。

可以用 `_` 处理暂时不关心的情况，但不要用它隐藏本应明确处理的业务状态：

```rust
fn is_quit(command: &Command) -> bool {
    matches!(command, Command::Quit)
}
```

## 解构与 if let

模式可以同时完成判断和取值：

```rust
let command = Command::Move { x: 2, y: 3 };

if let Command::Move { x, y } = command {
    println!("move: {x}, {y}");
}
```

当只关心一个变体时，`if let` 比只包含一个有用分支的 `match` 更紧凑；当多个状态都需要处理时，优先使用 `match`。

结构体也可以解构：

```rust
let user = User::new("Grace");
let User { name, active } = user;
println!("{name}: {active}");
```

解构会遵循所有权规则。若只想读取字段，使用引用模式或直接借用字段，避免不必要的 move。

## 常见误区

- 用一个 `bool` 或整数状态码代替 enum，容易产生非法组合。
- `match` 中用 `_` 过早吞掉未来新增的状态。
- 把构造器写成普通函数，导致调用处重复初始化逻辑。
- 解构 `String` 等拥有资源的字段时忘记它会发生 move。
- 用 `if let` 处理很多互斥状态，反而降低可读性。

## 自测

1. 哪些状态应该建模为 enum，而不是 struct 加一个状态字段？
2. 什么时候使用关联函数，什么时候使用方法？
3. `match` 的穷尽性检查为什么有价值？
4. 解构一个包含 `String` 的 struct 时，如何避免移动字段？

## 延伸

- [[Rust学习/02-类型系统/Option-Result-错误传播|Option、Result 与错误传播]]
- [[Rust学习/02-类型系统/泛型与Trait|泛型与 Trait]]
- 模式中的 `ref`、范围、守卫和 `@` 绑定
