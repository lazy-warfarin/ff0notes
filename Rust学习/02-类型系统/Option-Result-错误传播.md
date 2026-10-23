---
type: rust-concept
topic: option-result-error-handling
level: core
tags:
  - rust
  - option
  - result
  - error-handling
---

# Option、Result 与错误传播

## 要解决的问题

Rust 不用空指针或隐式异常表达失败：

- `Option<T>`：值可能存在，也可能缺失。
- `Result<T, E>`：操作成功得到 `T`，失败得到 `E`。

它们都是 enum，因此可以使用 `match`、`if let` 和组合器处理。

## Option：显式表示缺失

```rust
fn first_word(text: &str) -> Option<&str> {
    text.split_whitespace().next()
}

match first_word("rust language") {
    Some(word) => println!("first word: {word}"),
    None => println!("empty input"),
}
```

常见方法：

```rust
let value = Some(10);

let doubled = value.map(|n| n * 2);       // Some(20)
let fallback = value.unwrap_or(0);        // 10
let present = value.is_some();            // true
```

只有在确实能证明不可能失败时才使用 `unwrap` 或 `expect`。面向用户输入、文件和网络的代码应该显式处理 `None`。

## Result：显式表示成功或失败

```rust
fn parse_port(text: &str) -> Result<u16, std::num::ParseIntError> {
    text.parse()
}

match parse_port("8080") {
    Ok(port) => println!("port: {port}"),
    Err(error) => eprintln!("invalid port: {error}"),
}
```

`Result<T, E>` 让调用者决定失败策略：重试、返回错误、记录日志，或者在不可恢复的程序初始化阶段终止。

## `?`：让错误向上传播

如果当前函数返回的错误类型能够承接下层错误，就可以使用 `?`：

```rust
use std::num::ParseIntError;

fn parse_pair(input: &str) -> Result<(i32, i32), ParseIntError> {
    let mut parts = input.split(',');
    let left = parts.next().unwrap_or("").parse()?;
    let right = parts.next().unwrap_or("").parse()?;
    Ok((left, right))
}
```

`?` 做了两件事：

1. 成功时取出 `Ok` 内的值。
2. 失败时立即从当前函数返回 `Err`。

它不是 `unwrap` 的语法糖，也不会吞掉错误。

## 组合器

当逻辑简单时，组合器可以减少嵌套：

```rust
fn positive_port(text: &str) -> Option<u16> {
    text.parse::<u16>().ok().filter(|port| *port > 0)
}

let name = Some("rust");
let length = name.map(str::len);
```

常见组合器：

- `map`：转换成功值或存在值。
- `and_then`：继续一个也可能失败的操作。
- `map_err`：转换错误类型。
- `ok_or` / `ok_or_else`：把 `Option` 转成 `Result`。
- `unwrap_or` / `unwrap_or_else`：提供缺省值。

## 设计错误边界

- 预期可能发生的失败：返回 `Result` 或 `Option`。
- 程序逻辑不变量被破坏：可以使用 `assert!` 或 `expect`，并提供清晰消息。
- 绝不能恢复的初始化失败：在最外层统一处理，而不是在每个函数里随意 `unwrap`。

公共 API 应尽量返回有意义的错误类型。简单程序可使用标准库错误；复杂工程可以进一步定义自有 error enum。

## 常见误区

- 用 `unwrap` 代替错误设计，导致输入稍有变化就 panic。
- 把“值不存在”和“操作失败”都塞进 `Option`，丢失失败原因。
- 在函数内部打印并吞掉错误，让调用者无法决定处理策略。
- 使用 `?` 时忘记让函数返回 `Result` 或 `Option`。
- 误以为 `?` 会自动记录日志；它只负责控制流和错误转换。

## 自测

1. 什么时候用 `Option<T>`，什么时候用 `Result<T, E>`？
2. `?` 遇到 `Err` 时具体发生了什么？
3. 如何把 `Option<&str>` 转成带自定义消息的 `Result<&str, String>`？
4. 哪些位置可以接受 `expect`，哪些位置应该返回错误？

## 延伸

- [[Rust学习/02-类型系统/Struct-Enum-模式匹配|Struct、Enum 与模式匹配]]
- [[Rust学习/02-类型系统/泛型与Trait|泛型与 Trait]]
- `From`/`Into` 与错误类型转换
