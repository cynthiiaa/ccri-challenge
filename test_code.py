import pytest
import ccri_challenge
import numpy as np


@pytest.fixture()
def matrix():
    return [
        [-1, -2, -3, -4, -5],
        [-6,  -7, -8,  9, -10],
        [11, -12, -13, -14, -15],
        [-16, -17, -18, -19, -20]
    ]


@pytest.fixture()
def matrix2():
    return [
        [-1, -2, -3, -4, -5, -6, -7],
        [-8, -9, -10, -11, -12, -13, -14],
        [-15, -16, -17, -18, -19, -20, -33],
        [-21, -22, -23, -24, 25, -26, -34],
        [-27, -28, -29, -30, -31, -32, -35]
    ]


@pytest.fixture()
def matrix3():
    return [
        [-1, -2, -3, -4, -5],
        [-6,  -7, 8,  9, -10],
        [11, 12, 13, -14, -15],
        [16, 17, 18, -19, -20]
    ]


@pytest.fixture()
def matrix4():
    return [
        [3]
    ]


@pytest.fixture()
def matrix5():
    return [
        [-3]
    ]


@pytest.fixture()
def matrix6():
    return [
        [3, -1]
    ]


@pytest.fixture()
def matrix7():
    return [
        [3],
        [0]
    ]


@pytest.fixture()
def jagged_array():
    return [
        [-1, -2, -3, -4, -5, -6, -7],
        [-8, -9, -10, -11, -12, -13, -14],
        [-15, -16, -17, -18, -19, -20, -33, 18, -20, -5],
        [-21, -22, -23, -24, 25, -26, -34],
        [-27, -28, -29, -30, -31, -32, -35]
    ]


@pytest.fixture()
def large_array():
    arr = np.full((11, 11), -1)
    arr[6, 5] = 1
    arr[7, 3] = 5
    return arr


def test_find_positive_values(matrix):
    candidate_coordinates = ccri_challenge.find_positive_values(matrix)
    positive_values = sorted([matrix[coord[0]][coord[1]]
                              for coord in candidate_coordinates])
    assert positive_values[0] > 0


@pytest.mark.xfail
def test_find_negative_values(matrix):
    candidate_coordinates = ccri_challenge.find_positive_values(matrix)
    values = [matrix[coord[0]][coord[1]]
              for coord in candidate_coordinates]
    values.append(-5)
    values = sorted(values)
    assert values[0] > 0


def test_search_2d_array_N_equals_3(matrix):
    coordinates = ccri_challenge.find_positive_values(matrix)

    # N = 3
    matches = ccri_challenge.search_2d_array(matrix, coordinates, 3)
    correct = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3),
               (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
    assert matches == len(correct)


def test_search_2d_array_N_equals_6(matrix):
    coordinates = ccri_challenge.find_positive_values(matrix)

    # N = 6
    matches = ccri_challenge.search_2d_array(matrix, coordinates, 6)
    correct = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3),
               (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
    assert matches == len(correct)


def test_matrix3_N_equals_3(matrix3):
    coordinates = ccri_challenge.find_positive_values(matrix3)

    # N = 3
    matches = ccri_challenge.search_2d_array(matrix3, coordinates, 3)
    correct = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3),
               (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
    assert matches == len(correct)


def test_matrix2_N_equals_5(matrix2):
    coordinates = ccri_challenge.find_positive_values(matrix2)
    matches = ccri_challenge.search_2d_array(matrix2, coordinates, 5)
    correct = [
        (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)
    ]
    assert matches == len(correct)


def test_1_element(matrix4):
    coordinates = ccri_challenge.find_positive_values(matrix4)
    matches = ccri_challenge.search_2d_array(matrix4, coordinates, 100)
    correct = [(0, 0)]
    assert matches == len(correct)


def test_no_positives(matrix5):
    coordinates = ccri_challenge.find_positive_values(matrix5)
    matches = ccri_challenge.search_2d_array(matrix5, coordinates, 8)
    assert matches == 0


def test_single_row(matrix6):
    coordinates = ccri_challenge.find_positive_values(matrix6)
    matches = ccri_challenge.search_2d_array(matrix6, coordinates, 100)
    correct = [(0, 0), (0, 1)]
    assert matches == len(correct)


def test_single_column(matrix7):
    coordinates = ccri_challenge.find_positive_values(matrix7)
    matches = ccri_challenge.search_2d_array(matrix7, coordinates, 20)
    correct = [(0, 0), (1, 0)]
    assert matches == len(correct)


def test_jagged_array_N_equals_0(jagged_array):
    coordinates = ccri_challenge.find_positive_values(jagged_array)
    matches = ccri_challenge.search_2d_array(jagged_array, coordinates, 0)
    assert matches == 2


def test_jagged_array_N_equals_4(jagged_array):
    coordinates = ccri_challenge.find_positive_values(jagged_array)
    matches = ccri_challenge.search_2d_array(jagged_array, coordinates, 4)
    assert matches == 31


def test_11x11_array(large_array):
    coordinates = ccri_challenge.find_positive_values(large_array)
    matches = ccri_challenge.search_2d_array(large_array, coordinates, 2)
    assert matches == 22
