# Data Structures and Algorithms
- [Data Structures and Algorithms](#data-structures-and-algorithms)
  - [Arrays](#arrays)
  - [Binary Search Trees](#binary-search-trees)
  - [Binary Trees](#binary-trees)
  - [Dynamic Programming](#dynamic-programming)
  - [Famous Algorithms](#famous-algorithms)
  - [Graphs](#graphs)
  - [Greedy Algorithms](#greedy-algorithms)
  - [Heaps](#heaps)
  - [Linked Lists](#linked-lists)
  - [Recursion](#recursion)
  - [Searching](#searching)
  - [Sorting](#sorting)
  - [Stacks](#stacks)
  - [Strings](#strings)
  - [Tries](#tries)
## Arrays
- if `multiple elements in an array are being compared` together, 
  - you can `create a hash table that stores the elements that frequently accessed`
  - if only a `specific value` in the hash value is needed, can create a `variable outside the hash table and check to update it every time the hash table is updated`
- if the `order of elements in an array can affect the comparison`, 
  - you can `sort the array and create left and right pointers`
  - if it is already sorted, `try to use pointers to avoid resorting`
- if an `entire sequence` must be validated
  - you can return `sequence index == sequence length`
## Binary Search Trees
- can be solved through `recursion`
- if using `recursion` to find solution, try to see if the space complexity can be optimized by `not stacking recursive function calls`
## Binary Trees
- if you have to `travel to each leaf node`, and `keep track of of their order` then `recursive function calls are expected`
- if you have to `travel to each leaf node`, and `keep track of of their order` then `recursive function calls are expected`
- when working recursively, `returning a special value for the lead node can be potentially useful`
- if using closures as helper functions, and they `increment or change a variable in the outside scope, check if the variable is mutable`
## Dynamic Programming
## Famous Algorithms
## Graphs
## Greedy Algorithms
A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage.
- If trying to `optimize on speed`, it may be useful to `sort as a first step`
## Heaps
## Linked Lists
## Recursion
## Searching
- The binary search algorithm works only with sorted arrays
  - if a problem involves a sorted array input, consider using the binary search algorithm
## Sorting
- `Bubble sorting` is when you iterate over a collection, compare adjacent elements, and swap accordingly. Repeating the cycle until, no swaps occur.
## Stacks
## Strings
## Tries