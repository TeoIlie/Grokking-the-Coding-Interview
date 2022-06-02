def binary_search(arr, key):
    # first assume ascending order only
    start = 0
    end = len(arr) - 1
    mid = (start + end)//2

    if arr[start] < arr[end]:
        ascending = True
    else:
        ascending = False

    while arr[mid] != key:
        if start > end:
            return -1
        # search correct half
        if key > arr[mid]:
            if ascending:
                start = mid + 1
            else:
                end = mid -1
        else: 
            if ascending:
                end = mid -1
            else:
                start = mid + 1
        mid = (start + end)//2

    return mid

def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()