# Pointers
- [Pointers](#pointers)
  - [Creating Pointers](#creating-pointers)
  - [Dereferencing Pointers](#dereferencing-pointers)
  - [The new Function](#the-new-function)
  - [Working with nil](#working-with-nil)
  - [Types With Internal Pointers](#types-with-internal-pointers)

## Creating Pointers 
```go
package main

import ("fmt")

func main() {
	var a int = 42
  
  // *int is a pointer to int type
	// & gets the address of a
  var b *int = &a
  fmt.Println(&a, b)	 
}
```
## Dereferencing Pointers
```go
package main

import ("fmt")

func main() {
	var a int = 42
	var b *int = &a
  fmt.Println(&a, b)

  // precede pointer with * to dereference the pointer
	fmt.Println(a, *b)
	 
}
```
## The new Function
```go
package main

import ("fmt")


func main() {
	var ms *myStruct
  // initializing a variable to a pointer to an object
  ms = &myStruct{foo: 21}
	fmt.Println(ms)
}

type myStruct struct {
	foo int
}
```
- another way to create pointers to an object
  - can't initialize the fields at the same time
```go
package main

import ("fmt")

func main() {
	var ms *myStruct
	ms = new(myStruct)
	
	// go dereference object pointers automatically
	ms.foo = 32 // (*ms).foo = 32
	fmt.Println(ms.foo) // fmt.Println((*ms).foo)
}

type myStruct struct {
	foo int
	bar string
}
```
## Working with nil
```go
package main

import ("fmt")


func main() {
	var ms *myStruct
  
  // print uninitialized pointer: <nil>
  fmt.Println(ms)

  // initializing a variable to a pointer to an object
  ms = &myStruct{foo: 21}
	fmt.Println(ms)
}

type myStruct struct {
	foo int
}
```
## Types With Internal Pointers
- all assignment operations in Go are copy operations
- slices and maps contain internal pointers, so copies point to same underlying data

```go
package main

import ("fmt")

func main() {
  // since slices are made up of pointers, bot a, b change
	a := []int{1, 2, 3}
	b := a
	fmt.Println(a, b)
	a[1] = 31
	fmt.Println(a, b)

  // [1 2 3] [1 2 3]
  // [1 31 3] [1 31 3]
}
```
```go
package main

import ("fmt")

func main() {
	a := map[string]string{"foo": "bar", "baz": "buz"}
	b := a
	fmt.Println(a, b)
	a["foo"] = "qux "
	fmt.Println(a, b)

  // map[baz:buz foo:bar] map[baz:buz foo:bar]
  // map[baz:buz foo:qux ] map[baz:buz foo:qux ]
}
```