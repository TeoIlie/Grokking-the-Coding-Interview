def search_ceiling_of_a_number(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        print(start, mid, end)
        # found key
        if arr[mid] == key:
            return mid
        # key not in array
        elif start == end:
            print('key', key, 'arr[mid]', arr[mid])
            if key > arr[mid]:
                return mid + 1
            else:
                return mid - 1

        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

def main():
  print(search_ceiling_of_a_number([4, 6, 10], 5))
#   print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
#   print(search_ceiling_of_a_number([4, 6, 10], 17))
#   print(search_ceiling_of_a_number([4, 6, 10], -1))


main()