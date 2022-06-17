from collections import deque

def find_closest_elements(arr, K, X):
    result = deque()
    # 1. do a binary search to find closest element in arr to X
    closest_index = binary_search_closest_index(arr, X)
    result.append(arr[closest_index])
            
    # 2. search left and right of closest element w/ two pointers
    # to find K closest elements
    left, right = closest_index - 1, closest_index + 1
    while len(result) != K:
        # append either left or right element, depending on which is closer
        # and only if it exists
        if left >= 0 and right <= (len(arr) - 1):
            if abs(X - arr[left]) < abs(X - arr[right]):
                result.appendleft(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
        # if left or right has hit its limit, append from the other side
        elif left < 0:
            result.append(arr[right])
            right += 1
        else:
            result.appendleft(arr[left])
            left -= 1

    return list(result)


def binary_search_closest_index(arr, X):
    # if X is out of bounds of the array
    if X > arr[-1]:
        return len(arr) - 1
    elif X < arr[0]:
        return 0

    start, end = 0, len(arr) - 1
    while start <= end:
        middle = (start + end)//2
        if arr[middle] == X:
            return middle
            
        elif X > arr[middle]:
            start = middle + 1
        else:
            end = middle - 1

    if abs(X - arr[start]) < abs(X - arr[end]):
        return start
    else:
        return end

def main():
    print("'K' closest numbers to 'X' are: " +
            str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
            str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
            str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()