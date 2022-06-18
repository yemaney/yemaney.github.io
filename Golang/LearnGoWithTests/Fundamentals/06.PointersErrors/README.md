# Pointers and Errors

- `pointers`
  - go copies values when you pass them to functions/methods
  - if you are writing a function that needs to mutate state you'll need it to take a pointer to the thing you want to change
  - done with the `*variable` syntax
- `nil`
  - pointers can be nil
  - when a function returns a pointer, check if it is nil to avoid runtime exceptions
- `Errors`
  - errors are the way to signify failure when calling a function
- The `var` keyword allows us to define values global to the package.
  - can be set as global variables to be more useful
- `type CustomName OriginalType`: Create new type from existing ones
  - `CustsomName(inputs)` to create an instance of the type
- Implement the `String()` interface on a custom struct to define how type is printed when used with `%s`

