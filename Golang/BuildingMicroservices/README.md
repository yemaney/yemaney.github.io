# Building Microservices with Go

source: https://www.youtube.com/watch?v=VzBGi_n65iU&list=PLmD8u-IFdreyh6EUfevBcbiuCKzFk0EW_&index=2

## Notes

- episode 1
    - `http.HandleFunc` registers the handler function for the given pattern in the DefaultServeMux
    - `http.ListenAndServe` listens on the TCP network address addr and then calls Serve with handler to handle requests on incoming connections
