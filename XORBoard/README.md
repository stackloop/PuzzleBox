## XOR Board

Imagine you have an mxn board of bits, all initialized as zero. The operations you are allowed to do are flipping an entire row or column.
Write a program that takes in any mxn bit matrix and outputs True if it is possible to generate it using the operations above, False otherwise.

## Examples
```
matrix = [
    [0, 1],
    [0, 1]
]
```
Output: True.
From a zeroed matrix, you can just flip the second column.

```
matrix = [
    [0, 0],
    [1, 0]
]
```
Output: False.
No combinations of flipping a zeroed matrix would yield this result.
