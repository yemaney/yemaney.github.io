# Introduction

An algorithm is a step by step procedure to solve a problem.

## 1.1  Priori Analysis and Posteriori Testing

| Priori Analysis         | Posteriori Testing   |
| ----------------------- | -------------------- |
| Algorithm               | Program              |
| Language Independent    | Language dependent   |
| Hardware Independent    | Hardware dependent   |
| Time and Space Function | Watch time and bytes |

## 1.2 Characteristics of Algorithms

1. Input - 0 or more
2. Output - at least one output or result
3. Definiteness - must be logical enough to program
4. Finiteness - must have a way to stop
5. Effectiveness - must serve some purpose

## 1.3 How to Write and Analyze Algorithms

Criteria's:

1. Time
    - how much time does it take
1. Space:
    - how much memory will it consume

*represented in functions not actual measurements*

## 1.4 Frequency Count Method

Count the number of times each statement is executed.

For loops of n times:
- loop will execute n + 1 times, the 1 being the last check which fails
- everything under the scope of the loop executes n times

Complexity is always taken as a function:
- use frequency count method to get function ex) `f(n) = 3n^2 + 2`
- simplify expression to its biggest polynomial degree ex) `O(n^2)`

Example 1.
```py
a = [8, 3, 9, 7, 2]

def sum(a, n):
    s = 0               # 1 (one assignment operation)
    for i in range(n):  # n + 1 (condition is checked n+1 times)
        s += a[i]       # n (addition happens n times)
    return s            # 1 (return once)

# total time is 2n + 3
# degree one polynomial
# final time complexity function simplified to O(n)

# space
# A =n, n=s=i=1 -> n + 3
# O(n)
```

Example 2.
```py
# and b are nxn matrices

def add(a, b, n):
    for i in range(n):                  # n + 1
        for j in range(n):              # n * (n + 1)
            c[i][j] = a[i][j] + b[i][j] # n * n

# time
# 2n^2 + 2n + 1
# O(n^2)

# space
# matrices : a = b = c = n^ 2
# scalars : n = i = j = 1
# 3n^2 + 3
# O(n^2)
```
