
def search_min_diff_element(arr, key):
    if key > arr[-1]:
        return arr[-1]
    if key < arr[0]:
        return arr[0]

    start, end = 0, len(arr) - 1
    while start <= end:
        middle = (start + end)//2
        if arr[middle] == key:
            return arr[middle]
        elif key < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1

    if abs(arr[start] - key) < abs(arr[end] - key):
        return arr[start]
    else:
        return arr[end]


def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()