'''
File:			sorted_matrix.py
Project:		Practice Problems
File Created:	Sunday, March 10th 2024
Remote:			PracticeProblems at 'https://github.com/john-cinquegrana/PracticeProblems'
Author(s):		John Cinquegrana (alllegron@gmail.com)

Copyright 2024 John Cinquegrana (alllegron@gmail.com)

This file contains a practice problem taken from a mock Microsoft interview.
It came from the following video as question 1:

https://www.youtube.com/watch?v=QBX7RkhuyCA
'''

__author__		=	"John Cinquegrana"
__copyright__	=	"Copyright 2024 John Cinquegrana (alllegron@gmail.com)"



import random
import numpy as np

# Matrix 1
matrix1 = np.asarray([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Matrix 2
matrix2 = np.asarray([
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])

# Matrix 3
matrix3 = np.asarray([
    [19, 20, 21],
    [22, 23, 24],
    [25, 26, 27]
])

def find_num(mat, key):
    '''
    Given a matrix where both rows and columns are sorted, find the index of a
    given number. If the number is not in the matrix, return (-1, -1).

    We perform this in O(log n) time by first performing a binary search across
    the major diagonal of the matrix, and then subsequent binary searches
    across a single row/column.
    '''
    # Get the width and height of the matrix
    height = len(mat)
    width = len(mat[0])
    # The length of the square matrix
    n = min( len(mat), len(mat[0]) )
    # Perform a search across the major diagonal
    diag = [mat[i][i] for i in range(n)]
    high_index = binary_insert(diag, key)
    # Check to make sure the element can actually be in the matrix
    if high_index == n:
        return (-1, -1)
    # See if we already found the number
    if mat[high_index][high_index] == key:
        return (high_index, high_index)
    else:
        i = high_index - 1
        num = mat[i][i]
        print(f'checking num {num}')
        if num == key:
            return (i, i)
        elif num < key:
            # We know the number must be directly below or to the left
            # Check the column first
            if i < height - 1:
                column = mat[i+1:, i]
                # Return the index of the number if it exists in the column
                col_result = binary_search(column, key)
                if (col_result != -1):
                    return (i, col_result + i + 1)
            # Check the row second
            if i < width - 1:
                row = mat[i, i+1:]
                # Return the index of the number if it exists in the row
                row_result = binary_search(row, key)
                if (row_result != -1):
                    return (row_result + i + 1, i)
            else:
                return (-1, -1)

            
def binary_search(arr, key, low=0, high=None):
    high = len(arr) - 1 if high is None else high
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_insert(arr, key, low=0, high=None):
    high = len(arr) - 1 if high is None else high
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return low