# Looping
- [Looping](#looping)
  - [For Statement](#for-statement)
    - [Simple Loops](#simple-loops)
    - [Exiting Early](#exiting-early)
    - [Looping through collections](#looping-through-collections)

## For Statement
### Simple Loops
```go
package main

import (
	"fmt"
)

func main() {
    // initializer := 0, condition, incrementor
    // i scoped to for loop
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}

    // j scoped to main function
    j := 0
	for ; j < 10; j++ {
		fmt.Println(j)
	}    

    // incrementor inside the loop
	for i := 0; i < 10;  {
		fmt.Println(i)
        i++
	}

    // effectively a while loop
    // the two colons (;) around the condition are optional
    k := 0
	for ;k < 10 ; {
		fmt.Println(k)
        k++
	}
}
```
```go
package main

import (
	"fmt"
)

func main() {
    // multiple counters
	for i, j := 0, 0; i < 5; i, j = i+1, j+1 {
		fmt.Println(i, j)
	}
}
```
```go
package main

import (
	"fmt"
)

func main() {
    //  nested loops
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			fmt.Println(i * j)
		}
	}
}
```
### Exiting Early
```go
package main

import (
	"fmt"
)

func main() {

    k := 0
	for {
		fmt.Println(k)
        k++
        if k == 5 {
            // breaks out of closest loop
            break
        }
	}
}
```
```go
package main

import (
	"fmt"
)

func main() {
    // breaking out of outer loop
Loop:
	for i := 1; i <= 3; i++ {
		for j := 1; j <= 3; j++ {
			fmt.Println(i * j)
			if i*j >= 3 {
				break Loop
			}
		}
	}
}
```
```go
package main

import (
	"fmt"
)

func main() {

	for i := 0; i < 10; i++ {
        if i%2 == 0 {
            continue
        }
		fmt.Println(i)
	}
}
```
### Looping through collections
- can be done for slices, arrays, maps. strings and channels
- assign  `_` to key or value when you don't plan on using it
```go
package main

import (
	"fmt"
)

func main() {
	s := []int{1,2,3}
	for k, v := range s {
		fmt.Println(k, v)
	}
}
```