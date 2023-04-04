"""
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
"""

import time


# def bfs_recursive_n_steps(matrix, queue, visited, steps):
#     if not queue:
#         return

#     print("matrix", matrix)
#     print("queue", queue)
#     print("steps", steps)
#     current = queue.pop(0)
#     visited.add(current)
#     print("current", current)
#     print("visited", visited)

#     # Process current node
#     print(matrix[current[0]][current[1]])
#     print()

#     # Add neighbors to the queue
#     neighbors = get_neighbors(matrix, current, steps)
#     print("neighbors", neighbors)
#     for neighbor in neighbors:
#         if neighbor not in visited:
#             queue.append(neighbor)

#     # Recursively call bfs on the next node in the queue
#     bfs_recursive_n_steps(matrix, queue, visited, steps-1)


def bfs(matrix, start, steps):
    queue = [start]
    visited = set()
    # bfs_recursive_n_steps(matrix, queue, visited, steps)
    neighbors = get_neighbors(matrix, start, steps)
    for element in neighbors:
        visited.add(element)
    print("start:", start)
    print("looky", sorted(visited))


def get_neighbors(matrix, node, steps):
    neighbors = []
    row, col = node[0], node[1]
    rows, cols = len(matrix), len(matrix[0])

    for i in range(steps+1):
        if row-i or row+i == row:
            if col-i >= 0:
                neighbors.append((row, col - i))  # Left
            if col+i <= cols - 1:
                neighbors.append((row, col + i))  # Right
        if row-i >= 0:
            neighbors.append((row - i, col))  # Up
            k = steps-i
            while k >= 0:
                if col-k > 0:
                    neighbors.append((row-i, col - k))  # Left
                if col+k < cols - 1:
                    neighbors.append((row-i, col + k))  # Right
                k -= 1
        if row+i <= rows - 1:
            neighbors.append((row + i, col))  # Down
            k = steps-i
            while k >= 0:
                if col-k > 0:
                    neighbors.append((row + i, col - k))  # Left
                if col+k < cols - 1:
                    neighbors.append((row + i, col + k))  # Right
                k -= 1
        # if col-i >= 0:
        #     neighbors.append((row, col - i))  # Left
        # if col+i <= cols - 1:
        #     neighbors.append((row, col + i))  # Right

    return neighbors


def find_positive_values(matrix):
    max_row = len(matrix)
    max_col = len(matrix[0])
    positives = [(i, k) for i in range(max_row)
                 for k in range(max_col) if matrix[i][k] > 0]
    return positives


test = [
    [-1, -2, -3, -4, -5],
    [6,  7,   8,  9, -10],
    [11, 12, 13, -14, -15],
    [16, 17, 18, -19, - 20]
]

starting_points = find_positive_values(test)
bfs(test, starting_points[0], 3)

# print(find_positive_values(test))  # unit test this

"""
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
    [6,    7✅,   8✅,   9✅,  -10],
    [11✅, 12✅,  13✅,  -14,  -15],
    [16✅, 17✅,  18,   -19,   -20]
]


"""
