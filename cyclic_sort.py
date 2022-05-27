def find_missing_numbers(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1 # j represents the index where nums[i] belongs
    if nums[i] == i + 1: # nums[i] is what it should be
      i += 1
    elif nums[i] != i + 1 and nums[j] == nums[i]: # nums[i] is NOT what it should be, but where it should go is also nums[i], dont't swap
      i += 1
    elif nums[i] != i + 1 and nums[j] != nums[i]: # nums[i] is in the wrong position, and its correct position is not equal to nums[i], then swap
      nums[i], nums[j] = nums[j], nums[i]


  missingNumbers = []

  for i in range(len(nums)):
    if nums[i] != i + 1:
      missingNumbers.append(i + 1)

  return missingNumbers


def main():
  print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))


main()