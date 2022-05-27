from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
    depth = 1
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        for _ in range(levelSize):
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
            # first childless node is the minimum depth
            if not (curr_node.left or curr_node.right):
                return depth
        depth += 1 


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()