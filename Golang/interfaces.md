# Interfaces
- Interfaces define behavior 
## Basics
```go
package main

import (
	"fmt"
)

func main() {
	var w Writer = &ConsoleWriter{}
	n, err := w.Write([]byte("Hello Go!"))
	fmt.Println(n, err)
}

type Writer interface {
	Write([]byte) (int, error)
}

type ConsoleWriter struct {}

// implementing the interface
func (w *ConsoleWriter) Write(data []byte) (int, error) {
	n, err := fmt.Println(string(data))
	return n, err
}
```
- although interfaces are commonly defined along side structs, they can be created with any type
```go
package main

import (
	"fmt"
)

func main() {
	myInt := IntCounter(0)
	var inc Incrementor = &myInt
	for i := 0; i < 3; i++ {
		fmt.Println(inc.Increment())
	}

}

type Incrementor interface {
	Increment() int
}

type IntCounter int

func (ic *IntCounter) Increment() int {
	*ic++
	return int(*ic)
}
```
## Composing Interfaces
```go
package main

import (
	"fmt"
)

func main() {
	var res WaiterServer = &Restuarant{}
	res.wait("Yemane")
	res.serve("Yemane")
}

type Waiter interface {
	wait(name string) string
}

type Server interface {
	serve(name string) string
}

type WaiterServer interface {
	Waiter
	Server
}

type Restuarant struct{}

func (r *Restuarant) wait(name string) string {
	fmt.Println("May I take your order ", name)
	return name
}

func (r *Restuarant) serve(name string) string {
	fmt.Println("Serving your food! ", name)
	return name
}
```
```go
package main

import (
	"fmt"
)

func main() {
    // passing only the Waiter part of the Restuarant
	var res Waiter = &Restuarant{}
	res.wait("Yemane")

    // will not be implemented and will result in error
	res.serve("Yemane")
}
```
## Type Conversion
```go
func main() {
	var r WaiterServer = &Restuarant{}
	r.wait("Yemane")
	r.serve("Yemane")

    // type conversion
	rs := r.(WaiterServer)
	fmt.Println(rs)
}
```
### The Empty Interface
- interface with no methods
- every type in Go implements the empty interface
```go
package main

import (
	"fmt"
)

func main() {
	var myObj EmptyInterface = &Bartender{}
	if w, ok := myObj.(Waiter); ok {
		w.wait("Yemane")
	}
}

type EmptyInterface interface{}

type Waiter interface {
	wait(name string)
}

type Bartender struct{}

func (b *Bartender) wait(name string) {
	fmt.Println("Would you like a drink? ", name)
}
```
### Type Switches
```go
package main

import (
	"fmt"
)

func main() {
	// empty interface
	var myObj interface{} = 0
	switch myObj.(type) {
	case int:
		fmt.Println("myObj is an int")
	case string:
		fmt.Println("myObj is a string")
	default:
		fmt.Println("myObj is of unknown type")
	}
}
```
## Implementing with Value vs Pointers
- method set of `value` is all methods with value receivers
- method set of `pointer` is all methods, regardless of receiver type
## Best Practices
- Use many, small interfaces over large monolithic ones
- Don't export interfaces for types that will be consumed
- do export interfaces for types that will be used by package
- Design functions and methods to receive interfaces whenever possible