# Concurrency

- `goroutines` the basic unit of concurrency in go
- `anonymous functions`
  - don't need name
  - can be called as their defined
  - used to start each of the concurrent processes
- `channels` help organize and control the communication between the different processes
  - helps avoid race conditions
- `channel <- data` or `x :=channel` 
  - send statements to control the direction data moves in channels
- `go test -bench="."` to benchmark tests
- `go test -race` check fo race conditions

---
### quotes

Make it work, make it right, make it fast - Kent Beck

premature optimization is the root of all evil - Donald Knuth
