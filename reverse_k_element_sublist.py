
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self) -> str:
    return str(self.value)

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_every_k_elements(head, k):
    if k <= 1 or head is None:
        return head
    current, previous = head, None
    while True:
        # save relevant positions
        last_node_of_previous_part = previous
        last_node_of_sublist = current

        # do the reversal, ensuring you dont reach the end
        next = None
        i = 0
        while current is not None and i < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

    # previous is the first node of reversed sub-list,
    # next is the first node of the next part

        # make the necessary connections
        # connect beginning
        if last_node_of_previous_part is None:
            head = previous
        else:
            last_node_of_previous_part.next = previous
        
        # connect end
        last_node_of_sublist.next = next

        # if you have reached the end of the list, break
        if current is None:
            break
        previous = last_node_of_sublist
        head.print_list()

    return head


def main():
  head = Node(1)  
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_every_k_elements(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()






