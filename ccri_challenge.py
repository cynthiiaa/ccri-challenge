"""
Author: Cynthia Ukawu

Note
You have a 2d array where every element has a single singed (popsitive or negative) number

- The height of the array is the number of nested lists -- rows
- The width of the array is the number of elements in each nested list -- columns
- Cell locations are written as (row, column) or (Y,X)
- There's a distance threshold called N which is greater than or equal to 0
- Using Manhattan distance: |x1-x2|+|y1-y2|

[
    [1,2],
    [3,4]
]

[
    [1,2,3,4,5],
    [6,7,8,9,10]
]

We are interested in whether or not the cell has a positive number or a negative number

Questions:
Can we assume the width of each nested array is the same?
So we're getting a list of unique values near a positive number?

Ideas
* Need to find positive value and iterate from there
* What if all the values are negative?
* Implement a cache so that values don't get recomputed
    - replace neighbors = [] with a dictionary. Lookup would be constant time rather than linear

# using recursion
[
    [-1✅, -2✅,  -3✅,  -4,   -5],
    [6,    7✅,   8✅,   9✅,  -10],
    [11✅, 12✅,  13🚫,  -14,  -15],
    [16✅, 17🚫,  18,   -19,   -20]
]

# not using recursion
if you go up or down a column by i the number of steps you can take left or right should be reduced by i,
example: if you go down two you can either go left once or right once
example2: if you go up three, you can either go left zero times or right zero times (if N = 3)
[
    [-1✅, -2✅,  -3✅,  -4,   -5],
    [6⭐️,    7✅,   8✅,   9✅,  -10],
    [11✅, 12✅,  13✅,  -14,  -15],
    [16✅, 17✅,  18,   -19,   -20]
]

[
        [-1✅,   -2✅,   -3✅,   -4✅,     -5✅],
        [-6✅,   -7✅,    8⭐️,    -9✅,    -10✅],
        [-11✅,  -12✅,   -13✅,  -14✅,   -15✅],
        [-16🚫,    -17✅,    -18✅,  -19✅,  -20🚫]
]
"""
import time


def search_2d_array(matrix, start, steps):
    if len(start) < 1:
        print("Empty")
        return 0

    visited = set()
    for value in start:
        neighbors = get_neighbors(matrix, value, steps)
        visited.update(neighbors)
    return len(visited)


# Method that will find all the neighbors to the starting points
def get_neighbors(matrix, node, steps):
    neighbors = []
    row, col = node[0], node[1]
    # rows, cols = len(matrix), len(matrix[0])
    rows = len(matrix)

    # algorithm to move around the matrix
    for i in range(steps+1):
        if i > rows-1:  # takes care of large steps in the vertical direction
            return neighbors
        if row-i or row+i == row:  # stay on the same row
            if col-i >= 0:
                neighbors.append((row, col - i))  # Left
            if col+i <= len(matrix[i]) - 1:
                neighbors.append((row, col + i))  # Right
        if row-i >= 0:  # Move up
            if col < len(matrix[row-i]):
                neighbors.append((row - i, col))
            k = steps-i
            while k >= 0:
                if col-k >= 0 and col-k < len(matrix[row-i]):
                    neighbors.append((row - i, col - k))  # Left
                if col+k < len(matrix[row-i]):
                    neighbors.append((row - i, col + k))  # Right
                k -= 1
        if row+i <= rows - 1:  # Move down
            if col < len(matrix[row+i]):
                neighbors.append((row + i, col))
            k = steps-i
            while k >= 0:
                # make sure the cell exists if the array is jagged
                if col-k >= 0 and col-k < len(matrix[row+i]):
                    neighbors.append((row + i, col - k))  # Left
                if col+k < len(matrix[row+i]):
                    neighbors.append((row + i, col + k))  # Right
                k -= 1
    return neighbors


# Method that will find all the positive starting points
def find_positive_values(matrix):
    max_row = len(matrix)
    positives = [(i, k) for i in range(max_row)
                 for k in range(len(matrix[i])) if matrix[i][k] > 0]
    return positives
