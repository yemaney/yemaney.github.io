![Python](./../assets/python.svg){ align=left }

!!! Example "objective"

    Documenting what  I find to be most important to, understanding the core language features of python, and becoming proficient as a python programmer.

## Data Structures
### Sequences
#### Lists
A list is an **ordered and mutable** sequence of, usually homogenous, objects. It's size is not fixed, and it can contain any type of data. There are multiple ways to create a list in python.

=== "Literal"

    ``` py
    list1 = [0, 1, 2, 3, 4]

    print(list1)
    """
    [0, 1, 2, 3, 4]
    """
    ```

=== "Loop"

    ``` py
    list2 = [] 
    for i in range(5): # traditional for loop
        list2.append(i)
    
    print(list2)
    """
    [0, 1, 2, 3, 4]
    """
    ```
=== "Comprehension"

    ``` py
    list3 = [i for i in range(5)] # list comprehension

    print(list3)
    """
    [0, 1, 2, 3, 4]
    """
    ```
=== "Constructor"

    ``` py
    list4 = list((0,1,2,3,4))

    print(list4)
    """
    [0, 1, 2, 3, 4]
    """
    ```
#### Tuples
A tuple is an immutable sequence, usually containing heterogenous elements.
=== "Literal"

    ``` py
    tuple1= (0, 1, 2, 3, 4)

    print(tuple1)
    """
    (0, 1, 2, 3, 4)
    """
    ```

=== "Constructor"

    ``` py
    tuple2 = tuple(("Charmander", 4, True))

    print(tuple2)
    """
    ("Charmander", 4, True)
    """
    ```

#### Slicing
Sequences can be sliced using  `sequence[start:stop:step]`. Where start, stop, and step are integers.
```py
list1 = [0, 1, 2, 3, 4]

print(list1)        # entire list
print(list1[0:3])   # first 3 elements
print(list1[0::2])  # every second element
print(list1[::-1])  # list reversed
"""
[0, 1, 2, 3, 4]
[0, 1, 2]
[0, 2, 4]
[4, 3, 2, 1, 0]
"""
```

#### Unpacking
Tuple unpacking works with any iterable object,  the star symbol `*` can be used to capture excess items.
=== "Basic"

    ``` py
    a, b, *rest = range(5)

    print(a)
    print(b)
    print(rest)
    """
    0
    1
    [2, 3, 4]
    """
    ```

=== "Tuple Swapping"

    ``` py
    a, b = 1, 2 # two variables being assigned in the same line
    a, b = b, a # swapping the values of the variables
    
    print(a, b)
    """
    2, 1
    """
    ```

### Dictionaries
A dictionary is an object of key value pairs, where each key can be used to access it's respective value. They keys must be
a hashable type, but the values can be anything.
=== "Literal"

    ``` py
    dict1 = {'one': 1, 'two': 2, 'three': 3}

    print(dict1)
    """
    {'one': 1, 'two': 2, 'three': 3}
    """
    ```

=== "Loop"

    ``` py
    dict2 = {}
    for i in range(3):
        dict2[str(i)] = i

    print(dict2)
    """
    {'0': 0, '1': 1, '2': 2}
    """
    ```
=== "Comprehension"

    ``` py
    dict3 = {str(i):i for i in range(3)}

    print(dict3)
    """
    {'0': 0, '1': 1, '2': 2}
    """
    ```
=== "Constructor"

    ``` py
    dict4 = dict([('two', "Hoenn"), ('one', "Kanto"), ('three', "Unova")])

    print(dict4)
    """
    {'two': 'Hoenn', 'one': 'Kanto', 'three': 'Unova'}
    """
    ```
=== "Accessing Elements"

    ``` py
    nums = {'one': 1, 'two': 2, 'three': 3}

    # using dictionary['key'] notation to access value in dictionary
    print(f"key one maps to : {nums['one']}")
    """
    key one maps to : 1
    """
    ```
!!! Tip

    The `dictionary['key']` notation can be used to access values in dictionary. But will result in a `KeyError` if the key doesn't actually exist.

    - use the `dictionary.get(key, default)` to avoiding running into this error. If the key doesn't exist, python will return the default value. If no default value is provided, python will return `None`.

### Sets
A set is a collection of unique elements. Attempting to add an element that already exists inside the set, will result in no change.
=== "Literal"

    ``` py
    set1 = {1, 2, 3}

    print(set1)
    """
    {1, 2, 3}
    ```

=== "Loop"

    ``` py
    set2 = set()
    for i in range(3):
        set2.add(i)

    print(set2)
    """
    {0, 1, 2}
    """
    ```
=== "Comprehension"

    ``` py
    set3 = {i for i in range(3)}

    print(set3)
    """
    {0, 1, 2}
    """
    ```
=== "Constructor"

    ``` py
    set4 = set((1, 1, 2, 2, 3))

    print(set4)
    """
    {0, 1, 2}
    """
    ```

---

!!! Tip

    1. Build with `Comprehension` can be really useful, and is preferred. But do not sacrifice readability. If a comprehension gets large then an ordinary loop is appropriate.
    2. `Constructors` are usually only used when an iterable is being fed into it. Perhaps from some data source.
    3. Generally, lists are for looping; tuples for structs. Lists are homogeneous; tuples heterogeneous.  Lists for variable length. <sup>[1](https://twitter.com/raymondh/status/324664257004322817?lang=en)</sup>

## Control Flow
### If Else
The `If Else` statements can be used to check a condition before deciding whether or not to execute a block of code. The `Elif` keyword can be used to accommodate more than two condition.

=== "If Else"

    ``` py
    x = 10
    if x < 0:
        print("x is negative")
    else:
        print("x is positive")
    """
    x is positive
    """
    ```

=== "If Elif (Else if) Else"

    ``` py
    x = 10
    if x < 0:
        print("x is negative")
    elif x == 0:
        print("x is 0")
    else:
        print("x is positive")   
    """
    x is positive
    """ 
    ```
=== "Truthy / Falsy Objects"

    ``` py
    x = 0
    y = 1
    z = []
    if not x:
        print(x)
    if y:
        print(y)
    if not z:
        print(z)
    """
    0
    1
    []
    """
    ```

### For Loops
For loops can be used to iterate over the elements of a container object. Usually sequences like lists, but can also work with dictionaries or sets.

=== "With range"

    ``` py
    x = [1, 2, 3]
    for i in range(len(x)):
        print(i)

    """
    0
    1
    2
    """
    ```

=== "With in"

    ``` py
    x = [1, 2, 3]
    for i in x:
        print(i)

    """
    0
    1
    2
    """
    ```
=== "enumerate"

    ``` py
    x = ["a", "b", "c"]
    for i, letter in enumerate(x):
        print(i, letter)
    """
    0 a
    1 b
    2 c
    """
    ```
=== "zip"

    ``` py
    x = ["a", "b", "c"]
    y = ["pple", "anana", "oconut"]
    for start, end in zip(x, y):
        print("".join((start, end)))
    """
    apple
    banana
    coconut
    """
    ```
### While Loops
While loops execute a code block so long as a condition evaluates to true.
``` py
x = 0
while x < 3:
    print(x)
    x += 1
"""
0
1
2
"""
```
### Break, Pass, Continue
`Break, Pass, and Continue` are keywords in python, used with conditionals or loops to alter the control flow.

1. Break: Used to exit early
2. Pass: Used to mean "do nothing" when a certain condition should have no logic execute
3. Continue: Used to end the current iteration, and move to the next one
   
=== "Break"

    ``` py
    for i in range(1, 4): # loop over number 1,2,3
        print(i)
        if i % 2 == 0: # early exit when i is even
            print(f"{i} is even, early exit")
            break
    """
    1
    2
    2 is even, early exit
    """
    ```

=== "Pass"

    ``` py
    if 2 < 3:
        print("2 < 3")
    if 2 < 3:
        pass # do nothing
    """
    2 < 3
    """
    ```
=== "Continue"

    ``` py
    i = 0
    while i < 5:    # loop over 0, 1, 2, 3, 4
        if i % 2 == 0:  # move to next iteration if i is even
            i += 1
            continue
        print(i)    # only print i if it is odd
        i += 1
    """
    1
    3
    """
    ```

### Try, Except, Finally
`Try, Except, Finally` are keywords in python used for error handling.

1. Try: Used to define a code block to be tried first.
2. Except: Used to catch an error that occurs in the `Try` block, and define a code block to run.
3. Finally: Used to define a code block to always run at the end. Generally used for clean up code.

``` py
x = 3
try:
    x += "2"
    print(x)
except TypeError:
    x += int("2")
    print(x)
finally:
    print('finally block')
"""
5
finally block
"""
```

!!! Tip

    `except Exception:` can be used to catch every possible error that occurs. But it is better to catch explicit errors like `TypeError` so the conditions where the code breaks, is explicitly known.

## Functions
Functions are used to define a block of code that can be called at a later time. In python functions are first class objects, which gives them the following properties.

1. Can be assigned to a variable or element of a data structure
2. Can be passed in as an argument to function
3. Can be return as a result of a function

=== "Generic"

    ``` py
    def add(x: int, y: int) -> int:
        """ returns sum of x and y"""
        return 2 + y

    result = add(2, 2)
    print(result)
    """
    4
    """
    ```
=== "lambda"

    ``` py
    f = lambda x: 2 * x

    result = f(2)
    print(result)
    """
    4
    """
    ```

!!! info

    The lambda function is pythons version of anonymous functions. They should generally be very simple. Most cases will not require one.

### args and kwargs
The `*` and `**` can be used to unpack iterables and dictionaries respectively, when they are passed as arguments for a python function.

=== "args"

    ``` py
    def add(*args):
        """ returns sum of x and y"""
        for i in args:
            print(i) # printing args to verify what's being passed
            
        return sum(args) # using built-in sum function

    args = (1, 2, 3)
    result = add(*args)
    print("Total is", result)
    """
    1
    2
    3
    Total is 6
    """
    ```
=== "kwargs"

    ``` py
    def sentence_maker(greeting=None, adjective=None, punctuation="."):
        sentence = f"{greeting} I am {adjective} today{punctuation}"
        return sentence

    kwargs = {"greeting": "Hi", "adjective": "great"}

    sentence = sentence_maker(**kwargs)
    print(sentence)
    """
    Hi I am great today.
    """
    ```
### Closures and Decorators
- A closure is a function that `lives inside another function`, and has access to the the variables of that `enclosing scope`.
- A decorator is a function that `takes another function as an argument`, `perform some processing `with the decorated function, and `returns it or replace it` with anther function.


=== "Closures"

    ``` py
    def countdown_from_100():
        count = 100
        
        def countdown(new_value: int):
            nonlocal count # accessing count variable from nonlocal scope
            count -= new_value
            return count
        
        return countdown

    avg = countdown_from_100()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    """
    90
    79
    67
    """
    ```
=== "Decorator"

    ``` py
    import functools
    from time import perf_counter
    from typing import Callable

    def timer(func: Callable):

        @functools.wraps(func)
        def inner(*args, **kwargs):
            print("Beginning operation")
            t0 = perf_counter()
            res = func(*args, **kwargs)
            t1 = perf_counter()
            print(f"Executed in {t1-t0} secs")
            return res
        
        return inner

    @timer
    def add2(x: int):
        print(f"Adding 2 to {x}")
        return x + 2

    res = add2(2)
    print(res)
    """
    Beginning operation
    Adding 2 to 2
    Executed in 1.1799999999999311e-05 secs
    4
    """
    ```

!!! Tip

    1. `nonlocal` allows the inner function to access the enclosing scope. Similarity `global` can be used to access the global scope.
    2. `functools.wraps` makes sure the decorated function retains its metadata (eg. docstrings) after it has been decorated.
    3. `perf_counter` is used for time the function call duration.

## Type Hints
Python is a dynamically typed language, so variable types aren't declared as they can change over the course of the program lifetime.

Python allows the use of type hints. `Type hints` don't affect how the interpreter runs the program.

1.  Helps type checkers give warnings when you pass an object of a type not expected
2.  Helps IDE's autocomplete, as they can suggest type appropriate methods
3.  Improves the documentation of the code as the intent becomes more clear.

=== "Basic"

    ``` py
    def add(x: int, y: int) -> int: # function takes two arguments of type int
        return x + y                # and returns an int

    res1 = add(0, 1)
    res2 = add(0, 1.0)      # IDE's will red-underline 1.0 as it is a float
    print(res1, res2)       # program works as type hints don't affect interpreter
    """
    1 1.00
    """
    ```
=== "Multiple Types"

    ``` py
    # data expected to be a list of int or str
    def listFunction(data: list[str | int]) -> None:
        for element in data:
            print(type(element))
    
        return None
        
    data1 = [1, "hello"]
    listFunction(data)
    """
    <class 'int'>
    <class 'str'>
    """
    ```
=== "Callable (Functions)"

    ``` py
    from typing import Callable

    # Creating type hints for two possible functions
    addInts = Callable[[int, int], int]
    addFloats = Callable[[float, float], float]

    # Creating two functions that follow the type hints
    def addInt(x: int, y: int) -> int: 
        return x + y 

    def addFloat(x: float, y: float) -> float:
        return x + y

    # define a function that takes another function as an input
    def handler(func: addInts) -> int:
        x, y = 0, 1
        return func(x, y)

    result1 = handler(addInt)
    result2 = handler(addFloat) # addFloat will be underlined since it is the wrong type

    print(result1, result2)     # program works as type hints don't affect interpreter
    """
    1 1
    """
    ```
=== "Classes"

    ``` py
    from typing import Protocol

    class Worker(Protocol): # define protocol
        ...
        def run(self):
            ... # ... is a placeholder for behavior concrete class will implement 
            

    class Connecter: # Create a class that follows the protocol
        
        def run(self):
            print("Running...")
            
            
    def workerFunction(worker: Worker) -> None: # type hint using the protocol
        worker.run()
        return None

    conn = Connecter()
    workerFunction(conn)
    """
    Running...
    """
    ```

!!! note

    1. The `list[str | int]` syntax is supported natively starting `python3.10`. In previous version you can either
        * `from __future__ import annotations`
        * `from typing import List`
    2. `Protocols` is one way to define implicit interfaces. If you want to create explicit interfaces use `abc.ABC`


## Classes
Classes in python act as an instruction set, that `define the structure and behavior of an object`. An instance of the class, or an object that follows the class protocol can be created by calling the class definition using the `object = Class()` notation. Classes can have methods, which generally fall into three types: `normal methods`, `class methods`, and `static methods`.

  
=== "Basic"

    ``` py
    class Vector: # Define the custom class name

        # Define parameters required when instantiating an object
        def __init__(self,  x: float, y: float, z: float):
            # define variables that an instance can access
            self.x = x
            self.y = y
            self.z = z

        # Define custom method, requires self as an argument in order
        # to be able to access the instance variables
        def largest(self):
            return max(self.x, self.y, self.z)
        

    vec = Vector(3, 2, 5)   # Create an instance of the class
    largest = vec.largest() # Call the custom method
    
    print(f"largest component of vector is: {largest}")
    """
    largest component of vector is: 5
    """
    ```

=== "Class Method"

    ``` py
    from __future__ import annotations
    import math

    class Vector:

        def __init__(self,  x: float, y: float, z: float):
            self.x = x
            self.y = y
            self.z = z

        # use a class method decorator
        # required argument is cls, as this method has access to the class
        @classmethod
        def unit_vector(cls, x: float, y: float, z: float):
            "Custom factory for creating unit vectors"

            magnitude = math.sqrt(x * x + y * y + z * z)
            x, y, z = x / magnitude, y / magnitude, z / magnitude
            return cls(x, y, z)

    u = Vector.unit_vector(1, 2, 3)

    print(f"{u}, {u.x: .2f}, {u.y: .2f}, {u.z: .2f}")
    """
    <__main__.Vector object at 0x0000019653470FA0>,  0.27,  0.53,  0.80
    """
    ```

=== "Static Method"

    ``` py
    from __future__ import annotations
    import math

    class Vector:

        def __init__(self,  x: float, y: float, z: float):
            self.x = x
            self.y = y
            self.z = z
        
        # use static method decorator
        # has access to the class or object
        @staticmethod
        def compute_magnitude(x: float, y: float, z: float):
            magnitude = math.sqrt(x * x + y * y + z * z)
            return magnitude

    mag = Vector.compute_magnitude(1, 2, 3)
   
    print(f"{mag: .2f}")
    """
    3.74
    """
    ```

!!! note

    1. Normal methods take `self` as the first argument. They have access to the instance attributes and methods the `self.attribute or self.method()` syntax
    2. Class methods take `cls` as the first argument and have access to the class itself. They are generally used to create alternative factory methods.
    3. Static methods do not have access to either to instance attributes not the class. They are essentially normal functions appended to a class.

## Python Data Model
All data in python is represented by objects or by relations between objects<sup>[1](https://docs.python.org/3/reference/datamodel.html)</sup>. 
### Special Methods

!!! abstract

    Special methods an be explicitly called using the `object.__specialmethod__()` syntax, but they are meant to be called internally by the python interpreter. The interpreter knows to use these methods when they are triggered by either an built-in function or operator. For example, `abs(v)` instead of `v.__abs__()` or `v2 *2` instead of `v2.__mul__(2)`. 

    Reasons for using special methods.
    
    1. Predictability
        
        All objects in the standard python library are designed with special methods. Using special methods makes your custom classes work in the same way a standard object works. It also makes your objects behavior more predictable to any third party who uses it, since they will probably expect it to work like a standard object. 
    
    2. Style

        The `object.__specialmethod__()` syntax is ugly. It is also unnecessary, as every special method maps to an built-i function or operator. 

=== "Comparing normal and special methods"

    ``` py
    import math

    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def magnitude(self):
        return  math.sqrt(self.x * self.x + self.y * self.y)
    
        def __abs__(self): 
            return math.sqrt(self.x * self.x + self.y * self.y)
        
    v = Vector(1, 3)

    print(v.magnitude())
    print(abs(v))
    """
    3.1622776601683795
    3.1622776601683795
    """
    ```
=== "String representation"

    ``` py
    import math

    class Vector:
        def __init__(self, x: float, y: float):
            self.x = x
            self.y = y
        
        def __repr__(self):
            return f"Vector({self.x} , {self.y})"

    v = Vector(1, 3)
    
    print(v)
    """
    Vector(1 , 3)
    """
    ```
=== "Operator Overloading"

    ```py
    from __future__ import annotations


    class Vector:
        def __init__(self, x: float, y: float):
            self.x = x
            self.y = y

        def __repr__(self):
            return f"Vector({self.x} , {self.y})"

        def __eq__(self, __o: Vector) -> bool:
            return self.x == __o.x and self.y == __o.y

        def __mul__(self, other: float):
            return Vector(self.x * other, self.y * other)


    v1 = Vector(2, 4)
    v2 = Vector(1, 2)
    v3 = v2 * 2

    print(f"{v1}, {v2}")
    print(v1 == v2)
    print(f"{v1}, {v2}, {v3}")
    print(v1 == v3)
    """
    Vector(2 , 4), Vector(1 , 2)
    False
    Vector(2 , 4), Vector(1 , 2), Vector(2 , 4)
    True
    """
    ```

!!! note

    There are many special methods, but you shouldn't implement them if they are not needed. In general only use methods that make sense within the context of what your object is and how it people will expect to behave. For example, an `__add__` method may make sense for a vector class, but would not be appropriate for a flower class.

## Interfaces
### Abstract Base Classes

!!! abstract

    Abstract Base Classes (ABC) is a module in the standard python library that is used to create formal interfaces. Interfaces are defined by inheriting from `ABC`. Then classes meant to observe the interface rules, are defined by inheriting from the interface. The `abstractmethod` decorator can be used to flag methods you expect to be implemented in the real classes. If the decorated method is not implemented, then an error occurs.

=== "Implementing ABC"

    ``` py
    from abc import ABC, abstractmethod


    class Connector(ABC):

        @abstractmethod
        def connect(self): # defining a method our interface expects
            pass


    class SQLConnector(Connector):

        # implementing the method expected by the interface with inherit from
        def connect(self):
            print("connecting to sql database...")


    sqlc = SQLConnector()
    sqlc.connect()
    """
    connecting to sql database...
    """
    ```

=== "Failing To Implement ABC"

    ``` py
    from abc import ABC, abstractmethod


    class Connector(ABC):

        @abstractmethod
        def connect(self):
            pass


    class SQLConnector(Connector):
        pass # Not implementing the abstract method


    sqlc = SQLConnector() # IDE's will red underline
    """
    Traceback (most recent call last):
    File "c:\Users\yeman_s1h20q2\Yemane\yemaney.github.io\main.py", line 14, in <module>
        sqlc = SQLConnector()
    TypeError: Can't instantiate abstract class SQLConnector with abstract method connect
    """
    ```


!!! note

    Abstract base classes may seem very similar to Protocols<sup>[1](https://yemaney.github.io/articles/Python/Beginner/#type-hints)</sup> used for type hinting classes. The difference is that ABC's can the structure and behavior of classes that try to use it.

    Available decorators are not restricted to just defining regular methods. The available options that can be imported from abc.
    
    1. abstractmethod 
    2. abstractclassmethod
    3. abstractstaticmethod
    4. abstractproperty