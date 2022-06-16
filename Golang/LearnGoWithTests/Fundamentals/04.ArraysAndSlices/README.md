# Arrays and Slices

- `arrays` define size in declaration
- `slices` are like array
  - have fixed capacity but can create new ones from old ones using `slice = append(slice, additionalSlice)`
  - can slice slices using `[start:stop]` syntax
- `len` can get the length of of an array or slice
- `go test -cover` to get test coverage
- `reflect.DeepEqual` to compare slices
  - can reduce type safety of code
    - can use a wrapper function to handle type unsafety
- slices can be made of elements of any type, even other slices
  - ex) `[][]string`
