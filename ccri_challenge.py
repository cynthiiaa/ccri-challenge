# Author: Cynthia Ukawu

import sys
GREEN = '\033[92m'
RED = '\033[91m'


def search_2d_array(matrix, starting_point, steps):
    """
    Method will count up the total number of cells in a neighborhood

    matrix: 2d-arry to search
    starting_point: list of positive starting points
    steps: number of steps to take
    """
    if len(starting_point) < 1:
        return 0

    visited = set()
    for value in starting_point:
        neighbors = get_neighbors(matrix, value, steps)
        visited.update(neighbors)
    return len(visited)


def get_neighbors(matrix, node, steps):
    """
    Method that will find all the neighbors to the starting points

    matrix: 2d-array to search
    node: starting cell in the matrix
    steps: number of steps to take from the starting cell
    """
    neighbors = []
    row, col = node[0], node[1]
    rows = len(matrix)

    # algorithm to move around the matrix
    for i in range(steps+1):
        if i > rows-1:  # takes care of large steps in the vertical direction
            return neighbors
        if row-i >= 0:  # Move up
            k = steps-i
            while k >= 0:
                # make sure the cell exists if the array is jagged
                if col-k >= 0 and col-k < len(matrix[row-i]):
                    neighbors.append((row - i, col - k))  # Left
                if col+k < len(matrix[row-i]):
                    neighbors.append((row - i, col + k))  # Right
                k -= 1
        if row+i <= rows - 1:  # Move down
            k = steps-i
            while k >= 0:
                # make sure the cell exists if the array is jagged
                if col-k >= 0 and col-k < len(matrix[row+i]):
                    neighbors.append((row + i, col - k))  # Left
                if col+k < len(matrix[row+i]):
                    neighbors.append((row + i, col + k))  # Right
                k -= 1
    return neighbors


def find_positive_values(matrix):
    """
    Method that will find all the positive starting points

    matrix: 2d-array to be searched for positive values
    """
    max_row = len(matrix)
    positives = [(i, k) for i in range(max_row)
                 for k in range(len(matrix[i])) if matrix[i][k] > 0]
    return positives


if __name__ == "__main__":
    # file1 = sys.argv[1]
    file1 = "resources/arr1.txt"
    arr = []
    steps = 0
    actual_cells = 0

    with open(file1, 'r') as txtFile:
        for line in txtFile:
            row = [int(value.strip()) for value in line.split(",")]
            arr.append(row)
        steps = arr[0][0]
        actual_cells = arr[1][0]
        try:
            arr = arr[2:]
        except:
            print("Empty array")

    starting_points = find_positive_values(arr)
    answer = search_2d_array(arr, starting_point=starting_points, steps=steps)

    if actual_cells == answer:
        print(f"{GREEN}Success")
    else:
        print(
            f"{RED}Failure!\nGot {answer} cells when there should be {actual_cells} cells.")
