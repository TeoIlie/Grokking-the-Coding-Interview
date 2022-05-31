import copy

def find_subsets(nums):
    subsets = [[]]
    nums.sort()
    for i, num in enumerate(nums):
        next_start_modified = len(subsets)

        # if duplicate
        if i > 0 and num == nums[i-1]:
            start_index = curr_start_modified
        # if not duplicate
        else:
            start_index = 0
        n = len(subsets)

        # add subsets, adding only to the ones created on the previous
        # iteration if the current num is a duplicate 
        for j in range(start_index, n):
            curr = copy.deepcopy(subsets[j])
            curr.append(num)
            subsets.append(curr)
        curr_start_modified = next_start_modified
    return subsets


def main():

  print("Here is the list of subsets: " , str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " , str(find_subsets([1, 5, 3, 3])))


main()