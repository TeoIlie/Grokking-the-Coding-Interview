
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  return find_path_recursive(root, sequence, 0)


def find_path_recursive(node, sequence, seq_index=0):
  # if leaf
  if not (node.left or node.right):
    # halt if sequence index isnt at end of sequence
    if seq_index != len(sequence) - 1:
      return False
    return sequence[seq_index] == node.val
  # if inner node
  else:
    # halt if sequence index out of bounds or 
    # current sequence number doesn't match node value
    if seq_index > len(sequence) - 1 or sequence[seq_index] != node.val:
      return False
    else:
      # iterate down left, right branches
      seq_index += 1
      return (node.left and find_path_recursive(node.left, sequence, seq_index)) or (
        node.right and find_path_recursive(node.right, sequence, seq_index))



def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 1, 5])))
  # print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
  # print("Tree has path sequence: " + str(find_path(root, [1, 1, 7])))


main()