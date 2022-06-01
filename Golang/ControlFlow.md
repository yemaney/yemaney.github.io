# Control Flow
- [Control Flow](#control-flow)
  - [If Statements](#if-statements)
    - [Operators](#operators)
    - [If-else and if-else if statements](#if-else-and-if-else-if-statements)
  - [Switch Statements](#switch-statements)
    - [Simple Cases](#simple-cases)
    - [Cases With Multiple Tests](#cases-with-multiple-tests)
    - [Falling through](#falling-through)
    - [Type Switches](#type-switches)
    - [Break](#break)

## If Statements
```go
package main

import (
	"fmt"
)

func main() {
	if true {
		fmt.Println("This test is true")
	}
}
```
```go
package main

import (
	"fmt"
)

func main() {
	pokemon := map[string]string {
		"Charmander": "Kanto",
		"torchic":	"Hoenn",
		"Chimchar": "Sinnoh",
	
	}
	if pop, ok := pokemon["torchic"]; ok {
		fmt.Printf(pop)
	}
}
```
### Operators
```go
package main

import (
	"fmt"
)

func main() {
	number := 50
	guess := 24

	if guess < 1 || guess > 100 {
		fmt.Println("The guess must between 1 and 100")
	}

	if guess >= 1 && guess <= 100 {
		if guess < number {
			fmt.Println("To Low")
		}
		if guess > number {
			fmt.Println("To High")
		}
		if guess == number {
			fmt.Println("You got it!")
		}

		fmt.Println(number <= guess, number >= guess, number != guess)
	}
    fmt.Println(!true)
}
```
- go exits logical tests early (short circuiting)
  - escape or test on first true condition
  - escape and test on first false condition
### If-else and if-else if statements
```go
package main

import (
	"fmt"
)

func main() {

    // else statement
	number := 50
	guess := 24

	if guess < 1 || guess > 100 {
		fmt.Println("The guess must between 1 and 100")
	} else {
		if guess < number {
			fmt.Println("To Low")
		}
		if guess > number {
			fmt.Println("To High")
		}
		if guess == number {
			fmt.Println("You got it!")
		}

		fmt.Println(number <= guess, number >= guess, number != guess)
	}
}
```
```go
package main

import (
	"fmt"
)

func main() {
	number := 50
	guess := 24

	if guess < 1 {
		fmt.Println("The guess must be greater 1")
	} else if guess > 100 {
		fmt.Println("The guess must be less than 100")
	} else {
		if guess < number {
			fmt.Println("To Low")
		}
		if guess > number {
			fmt.Println("To High")
		}
		if guess == number {
			fmt.Println("You got it!")
		}

		fmt.Println(number <= guess, number >= guess, number != guess)
	}
}
```
- go exits on the first matching if-else if case
## Switch Statements
- special purpose if statements
- can't have overlapping cases
### Simple Cases
```go
package main

import (
	"fmt"
)

func main() {
	switch 1 {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	default:
		fmt.Println("not one or two")
	}  
}
```
### Cases With Multiple Tests
```go
package main

import (
	"fmt"
)

func main() {
	switch 1 {
	case 1, 3, 5:
		fmt.Println("one. three, or five")
	case 2, 4, 6:
		fmt.Println("two, four, or six")
	default:
		fmt.Println("not one through 6")
	}  
}
```
```go
package main

import (
	"fmt"
)

func main() {
    // initialize switch value
	switch i:= 2+3;i {
	case 1, 3, 5:
		fmt.Println("one. three, or five")
	case 2, 4, 6:
		fmt.Println("two, four, or six")
	default:
		fmt.Println("not one through 6")
	}  
}
```
```go
package main

import (
	"fmt"
)

func main() {
    // un-tgged switch statements
	i:= 10
    switch {
	case i <= 10:
		fmt.Println("less than or equal to ten")
	case i <= 20:
		fmt.Println("less than or equal to ten")
	default:
		fmt.Println("greater than 20")
	}  
}
```
### Falling through
- make go to next case
```go
package main

import (
	"fmt"
)

func main() {
    // fallthrough key word
	i:= 10
    switch {
	case i <= 10:
		fmt.Println("less than or equal to ten")
        fallthrough
	case i <= 20:
		fmt.Println("less than or equal to ten")
	default:
		fmt.Println("greater than 20")
	}  
}
```
### Type Switches
```go
package main

import (
	"fmt"
)

func main() {
    // interface can take any type assignment
	var i interface{} = 1
	
	// get i  type
    switch i.(type) {
	case int:
		fmt.Println("i is an int")
	case float32:
		fmt.Println("i is a float32")
	case string:
		fmt.Println("i is  a string")
	default:
		fmt.Println("i is another type0")
	}  
}
```
### Break
- exit a case statement early
```go
package main

import (
	"fmt"
)

func main() {
    // interface can take any type assignment
	var i interface{} = 1
	
	// get i  type
    switch i.(type) {
	case int:
		fmt.Println("i is an int")
        break
        fmt.Println("this wont be printed")
	case float32:
		fmt.Println("i is a float32")
	case string:
		fmt.Println("i is  a string")
	default:
		fmt.Println("i is another type0")
	}  
}
```