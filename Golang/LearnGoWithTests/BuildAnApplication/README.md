# Notes

1. Implement `http.Handler` to create web servers
2. `http.HandlerFunc` turns ordinary functions into http.Handlers
3. Use `httptest.NewRecorder` to pass in as a `ResponseWriter` to let you spy on the responses your handler sends
4. Use `http.NewRequest` to construct the requests you expect to come in to your system
5. Using `interfaces` and `mocking` allows your to start coding in small steps. Because you don't need to create large requirements (like a db) and focus on the logic.
6. TDD to drive out the interfaces you need
7. use `http.NewServeMux()` for routing
8. use `Type embedding`to compose new structs or interfaces. Should only expose what's appropriate
9. use `encoding/json` to serialize and deserialize json
10. `Seeker` interface to go to beginning of file
11. `sort.Slice` for sorting slices
12. `os.File` to handle files, `Truncate` to change size of file
13. `os.Stdin` and `bufio.Scanner` to read from standard input
14. test using `mypackage_test` package name to see how others use your code
15. export test helpers and stubs to make them easier to use and allow others importing the code easier ways to test
16. update package structure to include `folders for each separate application`. reuse domain code by importing module
17. `time.Afterfunc`: scheduling a function call after a specific duration
18. `time.After(duration)`: returns a chan Time when the duration has expired. So if you wish to do something after a specific time, this can help.
19. `time.NewTicker(duration)`: returns a Ticker which is similar to the above in that it returns a channel but this one "ticks" every duration, rather than just once. This is very handy if you want to execute some code every N duration.
20. `separation of concerns`: separate the responsibilities of dealing with user input and responses away from domain code
21. `messy tests`
    1. If your tests look messy try and refactor them
    2. If you've done this and they're still a mess it is very likely pointing to a flaw in your design
22. `function implementing an interface`: 
    1. When you define an interface with one method in it you might want to consider defining a MyInterfaceFunc type to complement it so users can implement your interface with just a function.
    2. In Go you can add methods to types, not just structs. This is a very powerful feature, and you can use it to implement interfaces in more convenient ways.
23. user helper functions to retry assertions and add timeouts
24. use go routines to ensure the assertions don't block anything and then use channels to let them signal that they have finished, or not
