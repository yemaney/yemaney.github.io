# Select

- `select` helps you wait on multiple channels
  - use `time.After` to prevent system from blocking forever
- `httptest` helps create reliable http tests
  - same interfaces as the "real" `net/http` servers
- `defer` allows you to call function after the end of the containing function
  - keep the instruction near where resource is created for clarity
- `struct{}` is the smallest data type available from a memory perspective
- `Always make channels`
  - using var declaration gives it a 0 value of nil, which won't allow you to pass data to it
