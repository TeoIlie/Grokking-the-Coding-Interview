from heapq import *


def find_k_largest_numbers(nums, k):
    # this solution is inefficient -> O(NlogN) time and O(N) space
    max_heap = []
    result = []

    for elem in nums:
        heappush(max_heap, -elem)
    print(max_heap)

    for _ in range(k):
        curr = heappop(max_heap)
        result.append(-curr)

    return result


def main():

  print("Here are the top K numbers: " + str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))
  print("Here are the top K numbers: " + str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
