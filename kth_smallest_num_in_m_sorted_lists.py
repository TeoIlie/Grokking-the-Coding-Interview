from heapq import *
from collections import deque

def find_Kth_smallest(lists, k):
    # use same algorithm as for merge k sorted lists
    # stop when the result is of length k
    # store tuples in heap: (value, list_index)

    # 1. add all first elements to the min_heap
    min_heap = []
    for i,list in enumerate(lists):
        if list is not None:
            heappush(min_heap, (list[0], i))

    list_indices = [1] * len(lists)
    result = deque()

    # 2. repeatedly append the smallest element in the heap to the result
    # and add the next element from the corresponding list, until all lists
    # are fully processed
    while len(result) < k:
        tuple = heappop(min_heap)
        num, list_index = tuple[0], tuple[1]
        result.append(num)

        # append the next element from list
        if list_indices[list_index] < len(lists[list_index]):
            next_elem = lists[list_index][list_indices[list_index]]
            heappush(min_heap, (next_elem, list_index))
            list_indices[list_index] += 1    
    
    return result[-1]


def main():
    print("Kth smallest number is: " + str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
    print('Kth smallest number is:', find_Kth_smallest([[5, 8, 9], [1, 7]], 3))


main()