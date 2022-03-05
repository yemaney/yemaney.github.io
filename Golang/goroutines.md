# Goroutines
- [Goroutines](#goroutines)
	- [Creating Goroutines](#creating-goroutines)
	- [Synchronization](#synchronization)
		- [WaitGroups](#waitgroups)
		- [Mutexes](#mutexes)
	- [Parallelism](#parallelism)
	- [Best Practices](#best-practices)

## Creating Goroutines
- use `go` keyword in front of function call
- when using anonymous functions, pass data as local variables (arguments)
```go
package main

import (
	"fmt"
	"sync"
)

var wg = sync.WaitGroup{}

func main() {
	var msg string = "Hello"
	wg.Add(1)

	go func(msh string) {
		fmt.Println(msg)
		wg.Done()	
	}(msg)

	wg.Wait()
}
```
## Synchronization

### WaitGroups
- use sync.WaitGroup to wait for groups of goroutines to complete
  - `Add` : to inform the wait group that here are more goroutines for it to wait on
  - `Wait`: block the goroutine that is called until with wait group is compleded
  - `Done`: let wait group that one of the goroutine is completed

### Mutexes
- Use `synce.Mutexe` and `synce.RWMutex` to protect data access
  - to ensure only one goroutine is manipulating the data at one time 

```go
package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup = sync.WaitGroup{}
var counter int = 0
var m sync.RWMutex = sync.RWMutex{}

func main() {
	for i := 0; i < 10; i++ {
		wg.Add(2)
		m.RLock()
		go sayHello()
		m.Lock()
		go increment()
	}
	wg.Wait()
}

func sayHello() {
	fmt.Printf("Hello #%v\n", counter)
	m.RUnlock()
	wg.Done()
}

func increment() {
	counter++
	m.Unlock()
	wg.Done()
}
```

## Parallelism
- By default , Go will use CPU threads equal to available cores
  - Change with `runtime.GOMAXPROCS`
  - More threads can increase performance, but to many can slow it down 
    - test when getting close to production

## Best Practices
- Don't create goroutines in libraries
  - let consumer control concurrency
- When creating a goroutine, know how it will end
  - avoid subtle memory leaks
- check for race conditions at compile time
```bash
go run -race main.go
```