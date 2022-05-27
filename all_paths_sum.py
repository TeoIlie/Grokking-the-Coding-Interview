from collections import deque


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, sum):
    # lets try storing predecessors in a dictionary, and then finding paths at the end
    # time O(N), space O(N) for dictionary
    allPaths = []
    predecessors = {}
    leafs = []
    stack = [(root, sum)]
    while stack:

        current_tuple = stack.pop()

        current = current_tuple[0]
        current_sum = current_tuple[1]

        new_sum = current_sum - current.val

        if new_sum == 0 and not (current.left or current.right):
            leafs.append(current.val)

        if current.right:
            predecessors[current.right.val] = current.val
            stack.append((current.right, new_sum))
        if current.left:
            predecessors[current.left.val] = current.val
            stack.append((current.left, new_sum))

    for leaf in leafs:
        path = deque()
        while leaf in predecessors:
            path.appendleft(leaf)
            leaf = predecessors[leaf]
        path.appendleft(root.val)
        path = list(path)
        allPaths.append(path)

    return allPaths


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()