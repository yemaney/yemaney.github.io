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
