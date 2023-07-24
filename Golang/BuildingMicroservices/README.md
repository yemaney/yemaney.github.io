# Building Microservices with Go

source: https://www.youtube.com/watch?v=VzBGi_n65iU&list=PLmD8u-IFdreyh6EUfevBcbiuCKzFk0EW_&index=2

## Notes

- episode 1
    - `http.HandleFunc` registers the handler function for the given pattern in the DefaultServeMux
    - `http.ListenAndServe` listens on the TCP network address addr and then calls Serve with handler to handle requests on incoming connections
- episode 2
    - organize project by moving handlers to their own package
    - `http.NewServeMux` create a  serve mux if you don't want to use default one
    - `http.Server` create server with custom config like `IdleTimeout`
    - `go func()` to run server in goroutine
    - `make(chan os.Signal, 1)` to make channel for signals and `signal.Notify` to send shutdown signals
    - `http.Server.Shutdown` to gracefully shutdown when a signal is sent to the signal channel
