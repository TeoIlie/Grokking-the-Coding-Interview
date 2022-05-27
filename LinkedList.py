# class Node holds a value 'value' and a pointer 'next'
class Node:
    # initialize node with optional value
    def __init__(self, value=None):
        self.value = value
        self.next = None

    # overwrite print method to output Node value
    def __str__(self) -> str:
        return f"The value of the node is {str(self.value)}."


# class LinkedList holds linked Node objects
class LinkedList:

    # initialize a LinkedList with a head, default is None
    def __init__(self, head=None):
        self.head = head

    # print out the linked list
    def __str__(self) -> str:
        output = ""
        curr_node = self.head
        while curr_node is not None:
            if curr_node.next != None:
                output += (curr_node.value) + ', '
            else:
                output += (curr_node.value) + '.'
            curr_node = curr_node.next

        return output

    # append at a node at the beginning of the linked list
    def append_at_beginning(self, new_node):
        new_node.next = self.head
        self.head = new_node

    # append at the end of a linked list
    def append_at_end(self, new_node):
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

# Testing
if __name__ == "__main__":
    monday = Node("Monday")
    print(monday)
    tuesday = Node("Tuesday")
    print(tuesday)
    wednesday = Node("Wednesday")
    print(wednesday)

    temp = LinkedList(monday)
    temp.append_at_beginning(tuesday)
    print(temp)
    temp.append_at_end(wednesday)
    print(temp)




