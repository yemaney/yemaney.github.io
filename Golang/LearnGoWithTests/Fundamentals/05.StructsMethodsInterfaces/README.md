# Struct, Methods, & Interfaces

- `struct` is a named collection of fields where you can store data
- can access fields of a struct with `struct.field` syntax
- `g` will print a `more precise decimal` number than `f`
- `method` is a function with a receiver (a struct)
  - called by invoking them on an instance of a particular type
- `interface` define functions that can be used by different types
  - if a struct has those methods then they implement the interface
  - used to decouple as the internals of a struct can be hidden if they are referred to thorough there interface
- `table driven tests` are used to test a list of test cases that can be tested in the same manner
- `%#v` will print a struct with the fields and values
- 