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
