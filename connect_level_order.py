from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot 
      nextLevelRoot = None 
      while current: 
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left 
          elif current.right:
            nextLevelRoot = current.right
        current = current.next 
      print()


def connect_level_order_siblings(root):

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)

        curr_level = []
        for i in range(levelSize):

            curr_node = queue.popleft()            
            if i < levelSize - 1:
                curr_node.next = queue[0]

            curr_level.append(curr_node.val)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
    
    return


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()