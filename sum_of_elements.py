from heapq import *

def find_sum_of_elements(nums, k1, k2):
    # store all elements in a min heap
    # pop k1 smallest elements from heap
    # sum (k2 - k1 - 1) elements from the heap and return 
    min_heap = []
    for i in range(len(nums)): # O(N * logN)
        heappush(min_heap, nums[i])
    for _ in range(k1): # O(k1 * logN), k1 < N
        heappop(min_heap)

    result = 0
    for _ in range(k2 - k1 - 1): # O((k2-k1-1) * logN), (k2-k1-1) < N
        result += heappop(min_heap)

    # overall time complexity: O(N * logN)
    # overall space O(N)
    return result


def find_sum_of_elements_v2(nums, k1, k2):
  maxHeap = []
  # keep smallest k2-1 numbers in the max heap
  for i in range(len(nums)):
    if i < k2 - 1:
      heappush(maxHeap, -nums[i])
    elif nums[i] < -maxHeap[0]:
      heappop(maxHeap) # as we are interested only in the smallest k2 numbers
      heappush(maxHeap, -nums[i])

  # get the sum of numbers between k1 and k2 indices
  # these numbers will be at the top of the max heap
  elementSum = 0
  for _ in range(k2 - k1 - 1):
    curr = -heappop(maxHeap)
    print(curr)
    elementSum += curr

  return elementSum



def main():
    print("Sum of all numbers between k1 and k2 smallest numbers: " + str(find_sum_of_elements_v2([1, 3, 12, 5, 15, 11, 16], 3, 6)))
    # print("Sum of all numbers between k1 and k2 smallest numbers: " + str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()