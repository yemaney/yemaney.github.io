package v1

import "sync"

// keeps track of count
type Counter struct {
	mu    sync.Mutex
	value int
}

// increment counter value by 1. Uses mutex to add locks
func (c *Counter) Inc() {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.value++
}

// return current value of counter
func (c *Counter) Value() int {
	return c.value
}
