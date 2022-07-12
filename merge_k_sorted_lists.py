from __future__ import print_function
from heapq import *


class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None
  def __str__(self) -> str:
    result = ""
    while self is not None:
      result += str(self.value) + " "
      self = self.next
    return result


def merge_lists(lists):
  resultHead = None
  min_heap = []
  # 1. add all first elements to the min_heap
  for i,list in enumerate(lists):
    heappush(min_heap, (list.value, i))

  # 2. repeatedly append the smallest element in the heap to the result
  # and add the next element from the corresponding list, until all lists
  # are fully processed
  while min_heap:
    
    # add the smallest element from heap to result
    curr_tuple = heappop(min_heap)
    curr_node = ListNode(curr_tuple[0])
    if resultHead is None:
      resultHead = curr_node
    else:
      prev_node.next = curr_node
    prev_node = curr_node

    # add next item from list
    list_index = curr_tuple[1]
    lists[list_index] = lists[list_index].next
    if lists[list_index] is not None:
      heappush(min_heap, (lists[list_index].value, list_index))

  return resultHead


def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  print(result)


main()
