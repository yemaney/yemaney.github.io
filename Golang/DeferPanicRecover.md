# Defer, Panic, Recover
- [Defer, Panic, Recover](#defer-panic-recover)
  - [Defer](#defer)
  - [Panic](#panic)
  - [Recover](#recover)

## Defer
- `defer` delays statement execution until function exits
- LIFO ordered
- use cases; closing resources
  - group `open` and `close` functions together
- evaluates arguments at the time defer is called
```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println("start")
	defer fmt.Println("middle")
	fmt.Println("end")
}
```
## Panic
- return an error to user when program cannot continue at all
- occur after defer statements
```go
package main

import (
	"fmt"
)

func main() {
		fmt.Println("start")
		panic("something bad is happening")
		fmt.Println("end")
}
```
## Recover
- Used to recover from panics
- Only useful in deferred functions
- Current function will not continue, but higher functions in call stack will
  
```go
package main

import (
	"fmt"
	"log"
)

func main() {
		fmt.Println("start")
		panicker()
		fmt.Println("end")
}

func panicker() {
	fmt.Println("About to panic")
	defer func() {
		if err := recover(); err != nil {
			log.Println("Error: ", err)
            // repanic error if it can't be handled
            // panic(err)
		}
	}()
	panic("something bad happened")
}
```