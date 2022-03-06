# Arrays Notes:

- if `multiple elements in an array are being compared` together, 
  - you can `create a hash table that stores the elements that frequently accessed`
  - if only a `specific value` in the hash value is needed, can create a `variable outside the hash table and check to update it every time the hash table is updated`
- if the `order of elements in an array can affect the comparison`, 
  - you can `sort the array and create left and right pointers`
  - if it is already sorted, `try to use pointers to avoid resorting`
- if an `entire sequence` must be validated
  - you can return `sequence index == sequence length`
