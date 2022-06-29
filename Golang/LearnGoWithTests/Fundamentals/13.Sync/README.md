# Sync

- `Mutex` allows us to add locks to data
  - helps when concurrent processes are updating the same data
- `WaitGroup` is a means of waiting for a group of goroutines to finish there jobs
- `mutex vs channels` : use channels when apssing ownership of data and mutexes for managing state
- `go vet` command used to alert you if there are subtle bugs in code