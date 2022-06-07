def find_max_in_bitonic_array(arr):
    start, end = 0, len(arr) - 1
    for _ in range(5):
        mid = (start + end)//2
        print(start, mid, end)
        # if arr[mid] is bitonic max, return it
        print(arr[mid-1], arr[mid], arr[mid+1])
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return arr[mid]
        elif arr[mid] > arr[mid - 1]:
            start = mid 
        else:
            end = mid
 

def main():
    print()
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print()
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print()
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print()
    print(find_max_in_bitonic_array([10, 9, 8]))


main()