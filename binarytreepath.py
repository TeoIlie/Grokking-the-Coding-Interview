
from turtle import left


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path_stack(root, sum):
    stack = []
    stack.append((root, sum))
    
    while len(stack) != 0:
        curr_node_tuple = stack.pop()
        curr_node = curr_node_tuple[0]
        curr_sum = curr_node_tuple[1]

        if not (curr_node.right or curr_node.left) and curr_node.val == curr_sum:
            return True

        new_sum = curr_sum - curr_node.val

        if curr_node.right:
            stack.append((curr_node.right, new_sum))
        if curr_node.left:
            stack.append((curr_node.left, new_sum))

    return False


def has_path(node, sum):
    print('node', node.val)
    print('sum', sum, '\n')
    if not (node.left or node.right): # if leaf
        if node.val == sum: # if correct sum return True
            return True
        else: # else return false
            return False
    else: # if not leaf
        new_sum = sum - node.val # calculate new_sum
        # recurse on children with new_sum
        if (node.left and has_path(node.left, new_sum)) or (node.right and has_path(node.right, new_sum)):
            return True
        else:
            return False


def depth_first_search_recursive(root):
    # if leaf node, return value as single-item list
    if root.left is None and root.right is None:
        return [root.val]
    # if internal node, return node value, followed by 
    # DFS on left branch and DFS on right branch
    else:
        left_branch = []
        right_branch = []
        if root.left:
            left_branch = depth_first_search_recursive(root.left)
        if root.right:
            right_branch = depth_first_search_recursive(root.right)
        return [root.val] + left_branch + right_branch


def depth_first_search_stack(root):
    traversal = []
    stack = [root]
    while stack:
        curr_node = stack.pop()
        traversal.append(curr_node.val)
        if curr_node.right:
            stack.append(curr_node.right)
        if curr_node.left:
            stack.append(curr_node.left)
    return traversal


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(depth_first_search_stack(root))
    # print("Tree has path: " + str(has_path_stack(root, 23)))
    # print("Tree has path: " + str(has_path_stack(root, 18)))


main()