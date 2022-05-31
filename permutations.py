import copy

def find_permutations(nums):
    result = [[]]
    for num in nums:
        new_result = []
        # add num in every position for every current permutation
        n = len(result)
        # for every current permutation
        for i in range(n):
            curr = result[i]
            # add num in every position
            for j in range(0, len(curr) + 1):
                new_permutation = copy.deepcopy(curr)
                new_permutation.insert(j, num)
                new_result.append(new_permutation)
        result = new_result
    return result


def main():
  print("Here are all the permutations: " , len(find_permutations([1, 3, 5, 6, 8, 10, 11, 12, 13, 14])))


main()