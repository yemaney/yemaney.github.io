# Essentials

## Arrays

- declare `type` and `size` of the array when created
- can be initialized with values upon creation and or populated afterwards
- elements in an array are access using the `array[idx]` syntax
- un initialized elements of an array have a `default value of 0`


```c++
#include <iostream>
using namespace std;

int main()
{
    // create an array of size 10
    // initialize the first four elements
    int A[10] = {1, 2, 3, 4};

    // for loop using incrementation of index
    for (int i = 0; i < 10; i++)
    {
        cout << A[i] << endl;
    }

    // for loop without using index
    for (int x : A)
    {
        cout << x << endl;
    }

    return 0;
}
```
