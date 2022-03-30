## Data Structures
### Sequences
#### Lists
A list is an **ordered and mutable** sequence of, usually homogenous, objects. It's size is not fixed, and it can contain any type of data. There are multiple ways to create a list in python.

=== "Literal"

    ``` py
    list1= [0, 1, 2, 3, 4]

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
    a, b, rest

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
### Sets
A set is a collection of unique elements. Attempting to add an element to a set, will result in no change.
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

!!! Tip

    1. Build with `Comprehension` can be really useful, and is preferred. But do not sacrifice readability. If a comprehension gets large then an ordinary loop is appropriate.
    2. `Constructors` are usually only used when an iterable is being fed into it. Perhaps from some data source.
    3. Generally, lists are for looping; tuples for structs. Lists are homogeneous; tuples heterogeneous.  Lists for variable length. <sup>[1](https://twitter.com/raymondh/status/324664257004322817?lang=en)</sup>
