from heapq import *

class KthLargestNumberInStream:

    # attributes
    k = 0
    min_heap = []

    # constructor
    def __init__(self, nums, k):
        # add k largest elements of nums to the min_heap
        self.k = k
        for num in nums:
            heappush(self.min_heap, num)
            if len(self.min_heap) > k:
                heappop(self.min_heap)

    def add(self, num):
        heappush(self.min_heap, num)
        heappop(self.min_heap)
        return self.min_heap[0]

    def __str__(self):
        return (f"k: {self.k} \nnums: {self.min_heap}\n")


def main():
    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    # print(kthLargestNumber)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    # print(kthLargestNumber)
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    # print(kthLargestNumber)
    print("4th largest number is: " + str(kthLargestNumber.add(4)))
    # print(kthLargestNumber)


main()
