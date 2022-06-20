from heapq import *

def find_maximum_distinct_elements(nums, k):
    distinct_count = 0
    min_heap = []
    # 1. store all numbers with frequencies > 1 in a min heap,
    # and add distinct numbers to a counter
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1
    for num, freq in freq_map.items():
        if freq == 1:
            distinct_count += 1
        else:
            heappush(min_heap, (freq, num))

    # 2. remove from heap, making numbers distinct
    while k > 0 and min_heap:
        freq, num = heappop(min_heap)

        # make num disctinct if k is large enough
        # make num distinct by subtracting freq-1 from k, if k is large enough
        if k >= (freq - 1):
            k -= (freq - 1)
            distinct_count += 1
        # else, make k = 0
        else:
            k = 0

    # 3. if heap has emptied, remove remaining k elements from distinct_count
    if min_heap:
        return distinct_count
    else:
        return distinct_count - k


def main():
    print("Maximum distinct numbers after removing K numbers: " +
            str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
            str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
            str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
