from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def zigzag_traverse(root):
    result = []
    queue = deque()
    queue.append(root)
    i = 0
    while queue:
        level_size = len(queue)
        curr_level = deque()
        for _ in range(level_size):
            curr_node = queue.popleft()

            if i % 2 == 1:
                curr_level.appendleft(curr_node.val)
            else:
                curr_level.append(curr_node.val)

            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        result.append(list(curr_level))
        i += 1

    return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(zigzag_traverse(root)))


main()