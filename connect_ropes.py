from heapq import *

def minimum_cost_to_connect_ropes(ropeLengths):
    # insert all elements in heap
    min_heap = []
    for curr in ropeLengths:
        heappush(min_heap, curr)

    # calculate min cost
    cost = 0
    while len(min_heap) > 1:
        new_rope = heappop(min_heap) + heappop(min_heap)
        cost += new_rope
        heappush(min_heap, new_rope)
    
    return cost


def main():

  print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
