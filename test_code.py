import pytest
import ccri_challenge


@pytest.fixture()
def matrix():
    return [
        [-1, -2, -3, -4, -5],
        [-6,  -7, -8,  9, -10],
        [11, -12, -13, -14, -15],
        [-16, -17, -18, -19, -20]
    ]

# @pytest.fixture()
# def matrix2():
#     return [
#         [-1, -2, -3, -4, -5],
#         [-6,  -7,   8,  -9, -10],
#         [-11, -12, -13, -14, -15],
#         [-16, -17, -18, -19, - 20]
#     ]


@pytest.fixture()
def matrix3():
    return [
        [-1, -2, -3, -4, -5],
        [-6,  -7, 8,  9, -10],
        [11, 12, 13, -14, -15],
        [16, 17, 18, -19, -20]
    ]


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
    matches = sorted(ccri_challenge.search_2d_array(matrix, coordinates, 3))
    correct = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3),
               (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
    assert matches == correct


def test_search_2d_array_N_equals_6(matrix):
    coordinates = ccri_challenge.find_positive_values(matrix)

    # N = 6
    matches = sorted(ccri_challenge.search_2d_array(matrix, coordinates, 6))
    correct = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3),
               (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
    assert matches == correct


def test_matrix3_N_equals_3(matrix3):
    coordinates = ccri_challenge.find_positive_values(matrix3)

    # N = 3
    matches = sorted(ccri_challenge.search_2d_array(matrix3, coordinates, 3))
    correct = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3),
               (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
    assert matches == correct
