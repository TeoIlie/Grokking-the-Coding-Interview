import math


class ArrayReader:

  def __init__(self, arr):
    self.arr = arr

  def get(self, index):
    if index >= len(self.arr):
      return math.inf
    return self.arr[index]


def search_in_infinite_array(reader, key):

    start, end = 0, 1
    while key > reader.get(end):    
        start = end + 1
        end = (end+1) * 2

    while start <= end:
        middle = (start + end)//2
        if reader.get(middle) == key:
            return middle
        if key < reader.get(middle):
            end = middle - 1
        else:
            start = middle + 1

    return -1


def main():
  reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
  print(search_in_infinite_array(reader, 16))
  print(search_in_infinite_array(reader, 11))
  reader = ArrayReader([1, 3, 8, 10, 15])
  print(search_in_infinite_array(reader, 15))
  print(search_in_infinite_array(reader, 200))


main()






