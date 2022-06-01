# Variables
- [Variables](#variables)
  - [Variable Declaration](#variable-declaration)
  - [Re-declaration and shadowing](#re-declaration-and-shadowing)
  - [Visibility](#visibility)
  - [Naming Conventions](#naming-conventions)
  - [Type Conversion](#type-conversion)

## Variable Declaration
```go
// declare  a variable and then assign a value
var i int
i = 42

// one-liner declare and assign
var j int = 42

// don't declare type, (let go interpret)
// generally the preferred method
k := 42
```
```go
// block of variable declaration at package level
var (
    name string = "Hello"
    date string = "Halloween"
    age int = 24
)
```
## Re-declaration and shadowing
- Variable can only be declared once within each scope, or an error will occur
- Variable with the inner most scope takes precedence (shadowing)
- all declared variable must be used

## Visibility
- lowercase variables are scoped to the package
  - all src files in that package have access to it
- uppercase variable, are exposed to the outside word

## Naming Conventions
- length of variable name should reflect the life of the variable
  - short names are preferred
- acronym should be in all uppercase (ex URL)

## Type Conversion
```go
// declare and set variable i
var i int = 42
// declare variable j
var j float32

// use type as a function to convert types
j = float32(i)
```
```go
// import to handle conversion to string
import ("strconv")


var i int = 42

//  integer to ascii
j = strconv.Itoa(i)

```