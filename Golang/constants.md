# Constants
- [Constants](#constants)
  - [Naming Convention](#naming-convention)
  - [Typed Constants](#typed-constants)
  - [Untyped Constants](#untyped-constants)
  - [Enumerated Constants](#enumerated-constants)
  - [Enumeration Expressions](#enumeration-expressions)

## Naming Convention
- all constants are preceded with the `const` keyword
- naming in `camelCase`
- value can't be changed
- has to be assignable at compile time 
- can be shadowed
```go
package main 

import ("fmt")

func main () {
    const myConst int = 42
    fmt.Printf("%v, %T", myConst, myConst)
}
```

## Typed Constants
- can be made up any of the primitive types

## Untyped Constants
- compiler can infer the type of a constant
- can handle implicit type conversion, if an untyped constant is used in a function
  - ```go
        const n = 22
        var b int16 = 28
        n + b // will be of type int16
    ```
```go
package main 

import ("fmt")

func main () {
    const myConst = 42
    fmt.Printf("%v, %T", myConst, myConst)
}
```
## Enumerated Constants
- first value of `iota` is 0, which may create a false match if some of your logic expects on of the enumerated types to be 0
```go
package main 

import ("fmt")

// const block
const (
    a = iota
    b = iota
    c = iota
)

const (
    a2 = iota
)

func main () {
    fmt.Printf("%v\n", a) // 0
    fmt.Printf("%v\n", b) // 1
    fmt.Printf("%v\n", c) // 2

    // iota scoped to const block
    fmt.Printf("%v\n", a2) // 0

}
```
- can use `_` as variable name, `write only variable`, for the first value if we don't care for it
## Enumeration Expressions
- can define enumeration values dynamically by using either arithmetic, bitwise, or bit-shifting operations
```go
package main 

import ("fmt")

// const block
const (
    // can offset values in const block
    a = iota + 5
    b
    c
)

func main () {
    fmt.Printf("%v\n", a) // 5
    fmt.Printf("%v\n", b) // 6
    fmt.Printf("%v\n", c) // 7
}
```
```go
package main 

import ("fmt")

// const block
const (
    isAdmin = 1 << iota
    isHeadquarters
    canSeeFinancial
)

func main () {
    var roles byte = isAdmin | canSeeFinancial
    fmt.Printf("%b/n", roles) // 101

    // apply bit mask to see if user has permission
    fmt.Printf("Is Admin? %v", isAdmin & roles == isAdmin) // true
}
```