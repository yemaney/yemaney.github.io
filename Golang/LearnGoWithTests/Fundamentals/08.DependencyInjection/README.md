# Dependency Injection

- by having familiarity with the `io.Writer` interface
  - we were able to use the `bytes.Buffer` in our tests
  - and the `use other writers` in the standard library to use our function in a command line or web server

- `test code`
  - if you can't test a function easily, it's usually because of dependencies being hard wired into a function or global state
  - dependency injection motivates you to inject a dependency via an interface to mock out the resource which enables testing
- `separate concerns`
  - decouple where data goes from how it is generated
- `allow code ot be reusable`
