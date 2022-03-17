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
  - [Data Structures](#data-structures)
    - [Arrays](#arrays-1)
    - [Hash Tables](#hash-tables)
    - [Linked Lists](#linked-lists-1)
    - [Stacks and Queues](#stacks-and-queues)
    - [Trees](#trees)
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
- `Bubble sorting` is when you iterate over each index of an array, compare adjacent elements, and swap accordingly. Repeating the cycle until no swaps occur.
- `Insertion sorting` is when you iterate over each index of an array, and while the element at an index is less than the one before it, swap the elements. Essentially pushing each element as far back as possible.
- `Selection sorting`is when you iterate over each index of an array. At each index, check every element at and after the current index, find the index of the smallest element. Swap the element with the smallest element with the element at the current index.
## Stacks
## Strings
## Tries

---
## Data Structures
### Arrays
- a linear collection of values that are accessible using numbered indexes

| Operation                          | complexity                    |
| ---------------------------------- | ----------------------------- |
| Accessing a value at given index   | O(1)                          |
| Updating a value at a given index  | O(1)                          |
| Inserting a value at the beginning | O(n)                          |
| Inserting a value in the middle    | O(n)                          |
| Inserting a value at the end       | `dynamic` O(1), `static` O(n) |
| Removing a value at the beginning  | O(n)                          |
| Removing a value in the middle     | O(n)                          |
| Removing a value at the end        | O(1)                          |
| Copying the array                  | O(n)                          |

### Hash Tables

| Operation                  | complexity |
| -------------------------- | ---------- |
| inserting a key/value pair | O(1)       |
| Removing a key/value pair  | O(1)       |
| Lookup a key/value pair    | O(1)       |

### Linked Lists
- nodes that hold a value along with a pointer to another node or null

```
# singly linked list
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> null
    
# double linked list
null <-> 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> null
```

| Operation                          | Time Complexity         |
| ---------------------------------- | ----------------------- |
| Accessing the head                 | O(1)                    |
| Accessing the tail                 | single-O(n) double-O(1) |
| Accessing a middle node            | O(n)                    |
| Inserting / Removing the head      | O(1)                    |
| Inserting / Removing the tail      | O(n) to access + O(1)   |
| Inserting / Removing a middle node | O(n) to access + O(1)   |
| Searching for a value              | O(n)                    |

### Stacks and Queues

- `stack` An array like data structure whose elements follow the `LIFO` rule

| Operation                                      | Time Complexity |
| ---------------------------------------------- | --------------- |
| Pushing an element onto the stack              | O(1)            |
| Popping an elemnt off the stack                | O(1)            |
| Peeking at the element on the top of the stack | O(1)            |
| Search for an element in the stack             | O(n)            |

- `queue` An array like data structure whose elements follow the `FIFO` rule

| Operation                                        | Time Complexity |
| ------------------------------------------------ | --------------- |
| Enqueuing an element into the queue              | O(1)            |
| Dequeuing an elemnt out of the queue             | O(1)            |
| Peeking at the element at the front of the queue | O(1)            |
| Search for an element in the queue               | O(n)            |

### Trees
- A data structure thar consists of nodes, each with some value and pointers in to child nodes, which recursively form `subtrees`

