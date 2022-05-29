
## Main function

```cpp
#include <iostream>

int main()
{
    std::cout << "Hello World!" << std::endl;
}
```
- `#include` : used to include libraries 
- `int main() {}` the entry point of a cpp program
- function can return a value to indicate if it succeeded or failed

*extra*
- `std::ednl` creats new line characters
- `std::cout` print to console

## comments

```cpp
#include <iostream>

int main()
{
    // single line comments

    /* 
    multi
    line
    comments
    */
}
```

## Errors

- compile time erros
    - bbinary won't be created
- runtime errors
    - binray created but doesn't act as expected
- warnings
    - issues not seriours enough for compiler to stop working

## Statements and Functions

- `statements`
    - basic unit of computation in a C++ program
    - end with a semicolon `;`
    - executed in order from top to bottom
- `function`
    - takes inputs and returns a value
    - reusable collections of code
