# Simple WebServer

```mermaid
flowchart LR
    Server --> /
    Server --> /hello
    Server --> /form

    / --> index.html
    /hello --> hello_func
    /form --> form_func

    form_func --> form.html
```