from concurrent.futures import process
from heapq import *

def print_matrix(m):
    for row in range(len(m)):
        for col in range(len(m[0])):
            print("%3d" % (m[row][col]), end='')
        print()

def find_Kth_smallest(matrix, k):
    result = []
    N = len(matrix)
    print_matrix(matrix)

    # we must also store which matrix values have been processed
    # we can do this by flagging them with -1
    
    # store in heap as (value, row_index, col_index)
    min_heap = []
    heappush(min_heap, (matrix[0][0], 0, 0))

    while k != 0:
        value, row_index, col_index = heappop(min_heap)

        new_row_index = row_index + 1
        if new_row_index < N and matrix[new_row_index][col_index] != -1:
            # push element below
            below = matrix[new_row_index][col_index]
            heappush(min_heap, (below, new_row_index, col_index))
            matrix[new_row_index][col_index] = -1

        new_col_index = col_index + 1
        if new_col_index < N and matrix[row_index][new_col_index] != -1:
            # push right element
            right = matrix[row_index][new_col_index]
            heappush(min_heap, (right, row_index, new_col_index))
            matrix[row_index][new_col_index] = -1

        k -= 1
    return value


def main():
    print("Kth smallest number is: " + str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()