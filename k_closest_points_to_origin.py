from math import *
from heapq import *

class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

def find_closest_points(points, k):
    result = []
    min_heap = []
    dict = {}
    for p in points:
        distance = sqrt(p.x ** 2 + p.y ** 2)
        dict[distance] = p
        heappush(min_heap, distance)
        
    for _ in range(k):
        curr_len = heappop(min_heap)
        curr_p = dict[curr_len]
        result.append(curr_p)

    return result


def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()

