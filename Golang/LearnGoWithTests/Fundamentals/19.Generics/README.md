# Generics


- generics
  - make functions/structs able to work with more than one type, reducing duplication
  - constrained function/structs to only work with one type at a time (can't mix apples and oranges)


- generics vs interface{} : similarities
  - both can be used to define types that accept many types
  - for example define a function that can work with both string and ints

- interface{}
  - Less safe (mix apples and oranges), requires more error handling
  - Less expressive, interface{} tells you nothing about the data
  - More likely to rely on reflection, type-assertions etc which makes your code more difficult to work with and more error prone as it pushes checks from compile-time to runtime

