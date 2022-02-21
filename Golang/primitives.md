# Primitive Types

- [Primitive Types](#primitive-types)
  - [Boolean type](#boolean-type)
  - [Numeric types](#numeric-types)
    - [Integers](#integers)
    - [Floating](#floating)
    - [Complex numbers](#complex-numbers)
  - [Text types](#text-types)

## Boolean type
```go
var n bool = false
var y bool = true
```
```go
// get boolean by comparing
n := 1 == 1 // true
m := 1 == 2 // false
```
```go
// every initialized variable has a default 0 value
// bool of 0 is false
var n bool
fmt.Printf("%v, %T", n, n)
```
## Numeric types
### Integers
- options
  - signed integers
    - int8, int16, int32, int64
  - unsigned integers
    - uint8, uint16, uint32, uint64

```go 
package main

import ("fmt")

// basic arithmetic operations
func main() {
  a := 10
  b := 3
  fmt.Println(a + b)
  fmt.Println(a - b)
  fmt.Println(a / b)
  fmt.Println(a % b)  
}
```
```go
package main

import ("fmt")

// basic bit operations
func main() {
  a := 10 // 1010
  b := 3 // 0011
  fmt.Println(a & b) // ANG 1011
  fmt.Println(a | b) // OR 1011
  fmt.Println(a ^ b) // XOR 1001
  fmt.Println(a &^ b)  // AND NOT 1000
}
```

```go
package main

import ("fmt")

// bit shifting
func main() {
  a := 8 // 2^3
  fmt.Println(a << 3) // 2^3 * 2^3 = 2^6
  fmt.Println(a >> 3) // 2^3 / 2^3 = 2^0
}
```
### Floating
```go
package main

import ("fmt")

// 
func main() {
  a := 3.14
  n = 13.9e10 // declare using exponential notation
}
```
- same arithmetic operators as integers are available
- bit operators are not available

### Complex numbers
```go
package main

import ("fmt")


func main() {
  // go parser understands the i literal as an imaginary number
  var n  complex64 = 1 + 2i
  fmt.Printf("%v, %T", n, n)

  var j  complex64 = complex(1, 2)
  fmt.Printf("%v, %T", j, j)

  // isolate the real and imaginary components
  fmt.Printf("%v, %T", real(n), imag(n))
}
```
- arithmetic operators available

## Text types
- string are UTF-8 and immutable
```go
package main

import ("fmt")

// 
func main() {
  s := "This is a string"
  fmt.Printf("%v, %T", s, s)

  // string can be sliced, type conversion required to get string back
  fmt.Printf("%v, %T", string(s[2]), s)

  // concatenation
  s2 := "This is also a string"
  fmt.Printf("%v, %T", s + s2, s + s2)

  // convert string to a collection of byes
  b := []byte(s)
  fmt.Printf("%v, %T", s, s)
}
```
- Rune is UTF-32