# Mocking


`Take a thin slice of functionality and make it work end-to-end, backed by tests.`

- `mocking` create interfaces that real code and test code can implement
  - allows you to use dependency injection
- `Spies` are a kind of mock which can `record how a dependency is used`. They can record the arguments sent in, how many times it has been called, etc.
  - introduce tight coupling with tests and implementation, use only if important
- `favour testing expected behavior` rather than the implementation
- if mocking code become complicated
  - The thing you are testing is having to do too many things
  - Your test is too concerned with implementation details
- `a lot of mocking points to bad abstraction in your code.`
