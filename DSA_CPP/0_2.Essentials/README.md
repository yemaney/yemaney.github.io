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

## Structures

2. Sign of structure
4. Accessing Members

```cpp
#include <iostream>
using namespace std;

struct Rectangle
{
    int length;
    int breadth;
};
// 2. size of struct is totoal memory consumed by all of its members
// definition doesn't consume memory, memory is only consumed when a
// variable is created

int main()
{
    // 3. Declaring a Structure
    struct Rectangle r;
    // 3.1 Declaration and initialization
    struct Rectangle w = {10, 5};

    cout << w.breadth << endl;

    // array of structs
    struct Rectangle shapes[2];
    shapes[0] = {1, 2};
    shapes[1] = {3, 4};

    // can also do
    // struct Rectangle shapes[2] = {{1, 2}, {3, 4}};

    cout << shapes[0].length << endl;
    cout << shapes[0].breadth << endl;
    cout << shapes[1].length << endl;
    cout << shapes[1].breadth << endl;

    return 0;
}
```

## Pointers
Address variable that stores address of data.
1. Accessing heap memory
2. access resources outside of the program
3. parameter passing

```cpp
#include <iostream>

using namespace std;

int main()
{
    // declaration and initialization of pointer
    int a = 10;
    int *p;
    // & = address
    p = &a;

    cout << a << endl;
    cout << &a << endl;
    cout << p << endl;
    cout << *p << endl;

    // pointers with arrays
    int A[5] = {1, 2, 3, 4, 5};
    int *q;
    q = &A[0];

    for (int i = 0; i < 5; i++)
    {
        cout << q[i] << endl;
    }

    // pointers with heap
    int *r;
    r = new int[5];
    r[0] = 1;
    r[1] = 10;
    r[2] = 100, r[3] = 1000;
    r[4] = 10000;

    for (int i = 0; i < 5; i++)
    {
        cout << r[i] << endl;
    }

    // pointer size is independent of data type
    cout << sizeof(p) << endl;
    cout << sizeof(r) << endl;

    // release memory in heap
    delete[] r;
}
```