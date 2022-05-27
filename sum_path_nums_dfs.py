class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
    all_nums = []
    find_sum_of_path_numbers_recursive(root, 0, all_nums)
    total = 0
    for elem in all_nums:
        total += elem
    return total


def find_sum_of_path_numbers_recursive(node, current_num, all_nums):    
    # perform DFS, and every time you hit a leaf append the path

    # add the current digit to the current number
    current_num = current_num * 10 + node.val

    # base case: if leaf, append path number
    if not (node.left or node.right):
        all_nums.append(current_num)
        
    else:
        if node.left:
            find_sum_of_path_numbers_recursive(node.left, current_num, all_nums)
        if node.right:
            find_sum_of_path_numbers_recursive(node.right, current_num, all_nums)
        


def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()