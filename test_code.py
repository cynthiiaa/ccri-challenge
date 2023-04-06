import pytest
import ccri_challenge


# @pytest.fixture()
# def matrix():
#     return [
#         [-1, -2, -3, -4, -5],
#         [6,  7,   8,  9, -10],
#         [11, 12, 13, -14, -15],
#         [16, 17, 18, -19, - 20]
#     ]

@pytest.fixture()
def matrix():
    return [
        [-1, -2, -3, -4, -5],
        [-6,  -7,   8,  -9, -10],
        [-11, -12, -13, -14, -15],
        [-16, -17, -18, -19, - 20]
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
