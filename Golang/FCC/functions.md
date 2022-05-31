# Functions
- [Functions](#functions)
  - [Basic Syntax](#basic-syntax)
  - [Parameters](#parameters)
  - [Return Values](#return-values)
  - [Anonymous Functions](#anonymous-functions)
  - [Functions as types](#functions-as-types)
  - [Methods](#methods)

## Basic Syntax
- lower case or uppercase name of function results in it being either public or internal to the package
```go
package main

import (
	"fmt"
)

// basic function scaffold
func main() {

}
```
## Parameters
- can be values, in which case Go will make a copy and pass to the function scope
- can also be pointers, in which case if the function make any changes the parameters, the changes persist outside of the functions scope
  - maps and slices have internal pointers referencing their underlying data, so function will always behave as if a pointers are being passed
```go
// arguments to function
func sayMessage(msg string, i int) {
	fmt.Println(msg)
	fmt.Println(i)
}
```
```go
// arguments to function
func sayMessage(msg string, name string) {
	fmt.Println(msg, name)
}


// go will infer type to be the same for msg and name
func sayMessage(msg , name string) {
	fmt.Println(msg, name)
}
```
```go
package main

import (
	"fmt"
)

func main() {
	msg := "Hello "
	name := "Yemane"
	sayMessage(&msg, &name)
	fmt.Println(msg, name)
}

// function takes pointers as arguments
func sayMessage(msg, name *string) {
	fmt.Println(*msg, *name)
	*msg = "Goodbye "
	*name = "Yemane!"
}
```
```go
package main

import (
	"fmt"
)

func main() {
	sum(1, 2, 3, 4, 5)
}

// variadic parameters
// values because a slice of all int passed
func sum(values ...int) {
	fmt.Println(values)
	result := 0
	for _, v := range values {
		result += v
	}
	fmt.Println(result)
}
```
## Return Values
```go
package main

import (
	"fmt"
)

func main() {
	s := sum(1, 2, 3, 4, 5)
	fmt.Println(s)
}

// must indicate return type in function signature
func sum(values ...int) int {
	fmt.Println(values)
	result := 0
	for _, v := range values {
		result += v
	}
	return result
}
```
```go
package main

import (
	"fmt"
)

func main() {
	s := sum(1, 2, 3, 4, 5)
	fmt.Println(s)
}

// named return variable
func sum(values ...int) (result int) {
	fmt.Println(values)
	for _, v := range values {
		result += v
	}
	return 
}
```
```go
package main

import (
	"fmt"
)

func main() {
	s := sum(1, 2, 3, 4, 5)
	fmt.Println(*s)
}

// must indicate return type in function signature
func sum(values ...int) *int {
	fmt.Println(values)
	result := 0
	for _, v := range values {
		result += v
	}
	return &result
}
```
```go
package main

import (
	"fmt"
)

func main() {
	d, err := divide(5.0, 0)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(d)
}

// multiple return value, err handling
func divide(a, b float64) (float64, error) {
	if b == 0 {
		return 0.0, fmt.Errorf("Cannot divide by zero")
	}
	return a / b, nil
}
```
## Anonymous Functions
```go
package main

import (
	"fmt"
)

func main() {
	// immediately invoked anonymous function
	func(name string) {
		fmt.Println("Hello ", name)
	}("Yemane")

	// anonymous function as a variable
	f := func(name string) {
		fmt.Println("Hello ", name, " Again")
	}
	f("Yemane")
}
```
## Functions as types
```go
package main

import (
	"fmt"
)

func main() {
	// declaring function type
	var divide func(float64, float64) (float64, error)
	
  divide = func(a, b float64) (float64, error) {
		if b == 0 {
			return 0.0, fmt.Errorf("Cannot divide by zero")
		}
		return a / b, nil
	}
	d, err := divide(5.0, 0)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(d)
}
```
## Methods
```go
package main

import (
	"fmt"
)

func main() {
	//
	g := greeter{
		greeting: "hello",
		name: "Go",
	}
	// use method
	g.greet()
}

// greeter struct
type greeter struct {
	greeting string
	name string
}

// method is a function that executes in a known context (type)
func (g *greeter) greet() {
	fmt.Println(g.greeting, g.name)
}
```