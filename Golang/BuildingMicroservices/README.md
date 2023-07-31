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
- episode 3
    - create a `data` package to organize code for data
    - `json.NewEncoder` to efficently write json
    - use `tags` to control what json fields a written and what their names are
    - check method before ServeHTTP in product handler
- episode 4
    - `json.NewDecoder` to turn json into struct
    - `r.URL.Path` to fine the /path after the url of the api that's hit
    - `strconv.Atoi` to convert string into an int
- episode 5
    - `github.com/gorilla/mux` frame work for servers
    - `sm.Methods(http.MethodGet).Subrouter()` create subroutes for different methods
    - `putRouter.HandleFunc("/{id:[0-9]+}", ph.UpdateProduct)` define path variables with regex
    - `vars := mux.Vars(r)` and `vars["id"]`: get variables from path that gorrilla parsed in handlers
    - `postRouter.Use(ph.MiddlewareProductValidation)` add middleware to a router
    - `ctx := context.WithValue` and `r = r.WithContext(ctx)`: update the request with context in middleware
    - `prod := r.Context().Value(KeyProduct{}).(*data.Product)` get variable from request context in main handler
