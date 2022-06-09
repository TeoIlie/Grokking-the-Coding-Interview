from heapq import heappop, heappush

def find_Kth_smallest_number(nums, k):
    max_heap = []

    # input first K elements in max_heap
    for i in range(k):
        heappush(max_heap, -nums[i])

    # iterate through remainder of array
    # if a new min is found (less than root of heap), replace it in the heap
    for i in range(k, len(nums)):
        if nums[i] < -max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])

    # kth smallest will be the root of the max_heap
    return -max_heap[0]


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    #   since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()