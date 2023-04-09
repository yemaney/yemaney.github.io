# Notes

1. Implement `http.Handler` to create web servers
2. `http.HandlerFunc` turns ordinary functions into http.Handlers
3. Use `httptest.NewRecorder` to pass in as a `ResponseWriter` to let you spy on the responses your handler sends
4. Use `http.NewRequest` to construct the requests you expect to come in to your system
5. Using `interfaces` and `mocking` allows your to start coding in small steps. Because you don't need to create large requirements (like a db) and focus on the logic.
6. TDD to drive out the interfaces you need
