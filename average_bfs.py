from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
    result = []
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        curr_level_sum = 0
        for _ in range(levelSize):
            curr_node = queue.popleft()
            curr_level_sum += curr_node.val
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        result.append(curr_level_sum / levelSize)
        
    return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()






