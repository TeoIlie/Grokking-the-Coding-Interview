from heapq import *


class MedianOfAStream:

  maxHeap = []  # containing first half of numbers
  minHeap = []  # containing second half of numbers

  @staticmethod
  def print_heaps(self):
    print('Min Heap:', self.minHeap)
    print('Max Heap', self.maxHeap, '\n')

  def insert_num(self, num):
    # either both the heaps will have equal number of elements or max-heap will have one
    # more element than the min-heap
    if not self.maxHeap or -self.maxHeap[0] >= num:
      heappush(self.maxHeap, -num)
      # balance heaps
      if len(self.maxHeap) > len(self.minHeap) + 1:
        heappush(self.minHeap, -heappop(self.maxHeap))
    else:
      heappush(self.minHeap, num)
      # balance heaps
      if len(self.minHeap) > len(self.maxHeap):
        heappush(self.maxHeap, -heappop(self.minHeap))


  def find_median(self):
    if len(self.maxHeap) == len(self.minHeap):
      # we have even number of elements, take the average of middle two elements
      return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

    # because max-heap will have one more element than the min-heap
    return -self.maxHeap[0] / 1.0



def main():
  medianObject = MedianOfAStream()
  medianObject.insert_num(3)
  medianObject.insert_num(1)

  print("The median is: " + str(medianObject.find_median()))
  MedianOfAStream.print_heaps(medianObject)

  medianObject.insert_num(5)
  print("The median is: " + str(medianObject.find_median()))
  MedianOfAStream.print_heaps(medianObject)

  medianObject.insert_num(4)
  print("The median is: " + str(medianObject.find_median()))
  MedianOfAStream.print_heaps(medianObject)


main()