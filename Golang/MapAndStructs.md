# Maps and Structs
- [Maps and Structs](#maps-and-structs)
  - [Maps](#maps)
    - [What are Maps](#what-are-maps)
    - [Creating Maps](#creating-maps)
    - [Manipulation](#manipulation)
  - [Structs](#structs)
    - [What are Structs](#what-are-structs)
    - [Creating Structs](#creating-structs)
    - [Naming Convention](#naming-convention)
    - [Embedding](#embedding)
    - [Tags](#tags)

## Maps
### What are Maps
- Maps are collections of key value pairs
- type has to be consistent between each key value pair
- slice, maps, and function cannot be key to a map
- unordered
- copies reference same underlying data
### Creating Maps
```go
package main

import ("fmt")

func main() {
    // map[key type]valueType{key:value,}
    statePopulation := map[string]int{
        "California": 39,
        "Texas": 27,
        "Florida": 20,
    }
    fmt.Println(statePopulation)
    // map[California:39 Florida:20 Texas:27]

    // creating  a map using make function
    statePop := make(map[string]int)
}
```
### Manipulation
```go
package main

import ("fmt")

func main() {
    statePopulation := map[string]int{
        "California": 39,
        "Texas": 27,
        "Florida": 20,
    }

    // accessing map items
    fmt.Println(statePopulation["Texas"])

    // add to map
    statePopulation["Georgia"] = 10
    fmt.Println(statePopulation["Georgia"])

    // delete from map
    delete(statePopulation, "Georgia")
    fmt.Println(statePopulation["Texas"])

    // check if key is in map
    pop, ok := statePopulation["Ohio"]
    fmt.Println(pop, ok) // 0 False

    // find number of elements in ma
    fmt.Println(len(statePopulation))

}
```
## Structs
### What are Structs
- collection of related information
- unlike maps and arrays, types of field in Structs can be anything
- copies create independent operators
  - use `new := &old` to make copies point to same references
### Creating Structs
```go
package main

import ("fmt")

type Pokemon struct {
    number int
    name string
    types []string
}

func main() {
    aPokemon := Pokemon{
        number: 004,
        name: "charmander",
        types: []string{
            "fire",
        },
    }
    fmt.Println(aPokemon)

    // access value from a struct
    fmt.Println(aPokemon.name)
    fmt.Println(aPokemon.types[0])
}
```
```go
package main

import ("fmt")

func main() {
    // anonymous struct
    d := struct{name string} {name: "John"}
    fmt.Println(d)
}
```
### Naming Convention
- uppercase struct name or strut field names if you want them to be exported
### Embedding
- Go support composition instead of inheritance

```go
package main

import ("fmt")

type Animal struct {
    Name string
    Origin string
}

type Bird struct {
    Animal
    speedKPH float32
    CanFly bool
}

func main() {
    b := Bird{}
    // Animal fields
    b.Name = "Swellow"
    b.Origin = "Hoenn"

    // bird fields
    b.speedKPH = 35
    b.CanFly = true 
    fmt.Println(b)

}
```
### Tags
- tags can act as documentation for struct fields
```go
package main

import (
	"fmt"
	"reflect"
)

type Animal struct {
	Name   string `required max:"100"`
	Origin string
}

func main() {
	t := reflect.TypeOf(Animal{})
	field, _ := t.FieldByName("Name")
	fmt.Println(field.Tag)

}
```