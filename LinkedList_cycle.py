
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self) -> str:
    return str(self.value)

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def len_cycle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            # find cycle length by keeping slow still and moving fast by one
            fast = fast.next
            length = 1
            while(fast != slow):
                fast = fast.next
                length += 1
            return length


def find_cycle_start(head):
    # TODO: Write your code here
    cycle_length = len_cycle(head)
    
    # have two pointers, and move the second one 'cycle_length' steps forward
    # then increment both until they are at the same node -> this is the start
    point1, point2 = head, head
    for i in range(cycle_length):
        point2 = point2.next

    while point1 != point2:
        point1 = point1.next
        point2 = point2.next
        
    return point1


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()