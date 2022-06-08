
def find_single_numbers(nums):
    num = 0
    for elem in nums:
        num ^= elem
        print(num)
    return [-1, -1]


def main():
#   print('Single numbers are:' + str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
  print('Single numbers are:' + str(find_single_numbers([2, 1, 2, 1, 3])))

main()