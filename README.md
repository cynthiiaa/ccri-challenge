# Coding Challenge

## Notes

You have a 2d array where every element has a single singed (popsitive or negative) number

- The height of the array is the number of nested lists -- rows
- The width of the array is the number of elements in each nested list -- columns
- Cell locations are written as (row, column) or (Y,X)
- There's a distance threshold called N which is greater than or equal to 0
- Using Manhattan distance: |x1-x2|+|y1-y2|

## Ideas

- Need to find positive value and iterate from there
- What if all the values are negative?
- Implement a cache so that values don't get recomputed
  - replace neighbors = [] with a dictionary. Lookup would be constant time rather than linear

### using recursion

|       |       |       |      |     |
| ----- | ----- | ----- | ---- | --- |
| -1✅  | -2✅  | -3✅  | -4   | -5  |
| 6⭐️  | 7✅   | 8✅   | -9✅ | -10 |
| -11✅ | -12✅ | -13🚫 | -14  | -15 |
| -16✅ | -17🚫 | -18   | -19  | -20 |

### not using recursion

if you go up or down a column by i the number of steps you can take left or right should be reduced by i,
example: if you go down two you can either go left once or right once
example2: if you go up three, you can either go left zero times or right zero times (if N = 3)

|       |       |       |      |     |
| ----- | ----- | ----- | ---- | --- |
| -1✅  | -2✅  | -3✅  | -4   | -5  |
| 6⭐️  | -7✅  | -8✅  | -9✅ | -10 |
| -11✅ | -12✅ | -13✅ | -14  | -15 |
| -16✅ | -17✅ | -18   | -19  | -20 |

|       |       |       |       |       |
| ----- | ----- | ----- | ----- | ----- |
| -1✅  | -2✅  | -3✅  | -4✅  | -5✅  |
| -6✅  | -7✅  | 8⭐️  | -9✅  | -10✅ |
| -11✅ | -12✅ | -13✅ | -14✅ | -15✅ |
| -16🚫 | -17✅ | -18✅ | -19✅ | -20🚫 |

## Evaluating new arrays

Arrays can be stored in a text file.

- The first line is the number of steps to take, N.
- The second line is the correct number of cells that are N steps aways from the cells with positive values
- The next line(s) will be used to create the 2d-arry that'll be search.

See `arr1.txt` for an example on formating.

## Running the Code

When running the code in the terminal, pass in the array text file you want to use.

> example: `python3 ccri_challenge.py arr1.txt`
