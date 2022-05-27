from asyncio import QueueFull
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None
  def __str__(self) -> str:
    return str(self.val)


def traverse(root):
    # append -> enqueue, popleft -> dequeue
    result = []
    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        
        currLevel = []
        for _ in range(levelSize):
            currNode = queue.popleft()
            
            currLevel.append(currNode.val)
            if currNode.left is not None:
                queue.append(currNode.left)
            if currNode.right is not None:
                queue.append(currNode.right)
        
        result.append(currLevel)

    return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()