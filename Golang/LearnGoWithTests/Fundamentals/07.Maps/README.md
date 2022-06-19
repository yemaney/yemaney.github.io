# Maps

- `maps` allow you to store items in a manner similar to a dictionary
  - can create a new type out of dictionary and add methods to it
  - `var dictionary = map[string]string{}` or `var dictionary = make(map[string]string)`
  - `d[word] = definition` adding or updating a key/value pair in the dictionary
  - `delete(d, word)` to delete key `word` from dictionary `d`
- can create custom types, that implement the error interface
  - improves reusability
  - declare with `const` to make them immutable
  - having specific errors gives better information about what went wrong