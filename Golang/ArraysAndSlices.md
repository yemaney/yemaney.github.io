# Arrays and Slices
- [Arrays and Slices](#arrays-and-slices)
  - [Arrays](#arrays)
    - [Array Creation](#array-creation)
    - [Array Built-in Functions](#array-built-in-functions)
    - [Working with arrays](#working-with-arrays)
  - [Slices](#slices)
    - [Slice Creation](#slice-creation)
    - [Slice Built-in functions](#slice-built-in-functions)
    - [Working with slices](#working-with-slices)

## Arrays
### Array Creation
```go
package main

import ("fmt")

func main () {
    //  arrays are fixed size collections of items of the same type
    // [num of elements]type{elements}
    grades := [3]int{1,2,3}
    fmt.Printf("Grades: %v", grades) // Grades: [1 2 3]

    // don't have to define size if creating array  literal
    grades2 := [...]int{1,2,3}

    // filling out array using indexes
    var students [3]string
    students[0] = "Lisa"
    student[1] = "Ahmed"
    student[2] = "Arnold"
    fmt.Printf("Students: %v", students)

}
```
### Array Built-in Functions
```go
package main

import ("fmt")

func main () {
    var students [3]string
    students[0] = "Lisa"
    student[1] = "Ahmed"
    student[2] = "Arnold"

    // built-in length function
    fmt.Printf("Number of Students: %v", len(students))
}
```
### Working with arrays
```go
package main

import ("fmt")

func main () {

    a := [...]int{1,2,3}

    // copying array
    b := a

    // copying an array can being expensive
    // point to same address as original array
    c := &a

    fmt.Printf(a)
    fmt.Printf(b)
    fmt.Printf(c)
}
```

## Slices
### Slice Creation
```go
package main

import ("fmt")

func main () {
    // initialize a slice
    a := []int{1,2,3}

    // copies naturally refer to same underlying data
    b := a
    fmt.Printf("Capacity: %v\n", cap(b))

    // slicing syntax
    s := []int{1,2,3,4,5,6,7,8,9,10}
    c := s[:]    // slice of all elements
    d := s[3:]   // slice from 4th element to the end
    e := s[:6]   // slice first 6 elements
    f := s[3:6]  // copy 4th through 6th element
    fmt.Println(s)
    fmt.Println(c)
    fmt.Println(d)
    fmt.Println(e)
    fmt.Println(f)    
}
```
- slice can be created out of arrays
### Slice Built-in functions
```go
package main

import ("fmt")

func main () {

    // create slice using the built in make function
    // make(slice type, num of elements, capacity)
    a := make([]int, 3, 100)
    fmt.Printf("Length: %v", len(a))
    fmt.Printf("Capacity: %v", cap(a))
}
```
### Working with slices
```go
package main

import ("fmt")

func main () {

    // adding to a slice
    a := []int{}
    fmt.Printf("Length: %v", len(a))
    fmt.Printf("Capacity: %v", cap(a))    
    
    a = append(a, 1, 2, 3)
    fmt.Printf("Length: %v", len(a))
    fmt.Printf("Capacity: %v", cap(a))

    // concatenate slices
    a = append(a, []int{1, 2, 3}...)
    fmt.Printf("Length: %v", len(a))
    fmt.Printf("Capacity: %v", cap(a))
}
```
```go
package main

import ("fmt")

func main () {
    a := []int{1,2,3,4}

    // shift slice (remove from beginning)
    b := a[1:]

    // pop slice, (remove from end)
    c:= a[:len(a)-1]
    fmt.Printf()

    // remove middle (3rd) element
    d := append(a[:2], a[3:]...)
}
```