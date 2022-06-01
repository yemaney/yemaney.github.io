
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

## Inputs and Outputs

- `std::cout` : print data to console
- `std::cin` : read data from the console
- `std::cerr` : print erros to the console
- `std::clog` : print log messages to the console

- `>>` and `<<` are used to indicate the direction that data travels; either from console to program or from program to console
- std::cin can be chained
- `std::getline(inputstream, buffertostoreinto)` used to grab lines with spaces

## C++ Program Execution Model

- program written in human readable c++
- program is compiled into a binary executable that is not readable by human
- program is ran in memory (RAM)
- program will execute the statments from top to bottom
- prgroam will jump to diffeerent memory addresses during execution, and that is where some optimization occcurs

## C++ core language Vs Standard library Vs STL

- `core` : basic rules and types that define how c++ programs run
- `standard library` : set of ready to use, highly specialized components that can be used in programs
- `STL` : a highly specialized part of the standard library
