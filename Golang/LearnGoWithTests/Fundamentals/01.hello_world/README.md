# Hello World

## General
- `go mod init <name>` to initialize your project as a go module
- `func`  define a function
- `varName := value` to declare a variable
- `const` keyword to define constants 
- `//` used to create comments
- functions can be created an assigned to variables within other functions
- function arguments must have types declared
- function return value must have type declared
- `(name type)` syntax is used to define a name return value
  - will create a "name" variable and assign a type appropriate zero value to it
  - can do `return` instead of `return name`
  - `default` in the `switch` case will be branched to if none of the other case statements match
  - `public` functions start with a `capital` letter and `private` ones start with a `lowercase`



## Testing
- separate domain code from side-effects
  - ie) separate the creation of a string from the act of printing it
- file name needs to follow pattern of `xxx_test.go`
- test function must start with the word TEST
- test function takes one argument only `t *testing.T`
- to use the *testing.T type, you need to import `"testing"`
- `t.Errorf` print a message when a test fails
- helper functions, it's a good idea to accept a `testing.TB`
- `t.Helper()`  tells the test suite that this method is a helper
  - line number reported will be in our function call rather than inside our test helper


Cycle
- Write a test
- make the compiler pass
- run the test, check if it fails
- write enough code to make code pass
- refactor

