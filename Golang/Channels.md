# Channels
- [Channels](#channels)
  - [Channel Basics](#channel-basics)
  - [Restricting Data Flow](#restricting-data-flow)
  - [Buffered Channels](#buffered-channels)
  - [Range Loops and Closing Channels](#range-loops-and-closing-channels)
  - [Select Statements](#select-statements)

## Channel Basics
- create a channel with `make` command
  - strong typed `make(chan int)`
- send and receive a message to and from an channel using arrow syntax
  - send: `ch <- val`
  - receiveL `val := <-ch`
- Can have multiple senders and receivers
```go
package main

import (
	"fmt"
	"sync"
)

var wg = sync.WaitGroup{}

func main() {
	ch := make(chan int)
	wg.Add(2)
	go func() {
		i := <-ch
		fmt.Println(i)
		wg.Done()
	}()
	go func() {
		ch <- 0
		wg.Done()
	}()
	wg.Wait()

}
```
## Restricting Data Flow
- by default channels are bidirectional
- channel can be cast to send only or receive only versions
  - send only: `chan <- int`
  - receive only: `<-chan int`
```go
package main

import (
	"fmt"
	"sync"
)

var wg = sync.WaitGroup{}

func main() {
	ch := make(chan int)
	wg.Add(2)
	go func(ch <-chan int) {
		i := <-ch
		fmt.Println(i)
		wg.Done()
	}(ch)
	go func(ch chan<- int) {
		ch <- 0
		wg.Done()
	}(ch)
	wg.Wait()

}
```
## Buffered Channels
- channels block 
  - sender side until receiver is available
  - receiver side until message is available
- buffered channels contain internal data stores
- Use buffered channels when send and receive have asymmetric loading

```go
package main

import (
	"fmt"
	"sync"
)

var wg = sync.WaitGroup{}

func main() {
	ch := make(chan int, 2)
	wg.Add(2)
	go func(ch <-chan int) {
		i := <-ch
		fmt.Println(i)
		j := <-ch
		fmt.Println(j)
		wg.Done()
	}(ch)
	go func(ch chan<- int) {
		ch <- 0
		ch <- 1
		wg.Done()
	}(ch)
	wg.Wait()

}
```
## Range Loops and Closing Channels
- use to monitor channel and process messages as they arrive
- loop exits when channel is closed 
```go
package main

import (
	"fmt"
	"sync"
)

var wg = sync.WaitGroup{}

func main() {
	ch := make(chan int, 2)
	wg.Add(2)
	go func(ch <-chan int) {
		for i := range ch {
			fmt.Println(i)
		}
		wg.Done()
	}(ch)
	go func(ch chan<- int) {
		ch <- 0
		ch <- 1
		close(ch)
		wg.Done()
	}(ch)
	wg.Wait()

}
```

```go
package main

import (
	"fmt"
	"sync"
)

var wg = sync.WaitGroup{}

func main() {
	ch := make(chan int, 2)
	wg.Add(2)
	go func(ch <-chan int) {
		for {
			if i, ok := <-ch; ok {
				fmt.Println(i)
			} else {
				break
			}
		}		
		wg.Done()
	}(ch)
	go func(ch chan<- int) {
		ch <- 0
		ch <- 1
		close(ch)
		wg.Done()
	}(ch)
	wg.Wait()

}

```
## Select Statements
- allows goroutine to monitor several channels at once
  - block if all channels block
  - if multiple channels receive value simultaneously, behavior is undefined
- no blocking select statement can involve a dealt case
```go
package main

import (
	"fmt"
	"time"
)

const (
	logInfo    = "INFO"
	logWarning = "WARNING"
	logError   = "ERROR"
)

type LogEntry struct {
	time     time.Time
	severity string
	message  string
}

var logCh = make(chan LogEntry, 50)
var doneCh = make(chan struct{})

func main() {
	go logger()
	logCh <- LogEntry{time.Now(), logInfo, "App is startting"}
	logCh <- LogEntry{time.Now(), logInfo, "App is shutting down"}
	time.Sleep(100 * time.Millisecond)
	doneCh <- struct{}{}
}

func logger() {
	for {
		select {
		case entry := <-logCh:
			fmt.Printf("%v - [%v]%v\n", entry.time.Format("2006-01-02"), entry.severity, entry.message)
		case <-doneCh:
			break
		}
	}
}
```