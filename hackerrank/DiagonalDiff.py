'''
    Given a square matrix, calculate the absolute difference between the sums of its diagonals.

    For example, the square matrix arr is shown below:
    1 2 3
    4 5 6
    9 8 9 
    The left-to-right diagonal 1+5+9=15 . The right to left diagonal 3+5+9=17 . Their absolute difference is 2.
'''
def diagonalDifference(arr):
    size = len(arr)
    max_pos = size -1
    assert size == len(arr[0]) # Check is square matrix
    # Begin the looping xD
    diag_a = sum(arr[x][x] for x in range(size))
    diag_b = sum(arr[x][max_pos-x] for x in range(size))
    # Return absolute diff
    return abs(diag_a - diag_b)

if __name__ == '__main__':
    arr = [
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]
    ]
    result = diagonalDifference(arr)
    print(result)