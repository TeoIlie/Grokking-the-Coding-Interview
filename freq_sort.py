from heapq import *

def sort_character_by_frequency(str):
    # 1. calculate each letter and its frequency in a dictionary
    # then store it in a max heap, using tuples for ordering
    dict = {}
    for char in str:
        if char not in dict:
            dict[char] = 0
        dict[char] += 1

    max_heap = []
    for letter, freq in dict.items():
        heappush(max_heap, (-freq, letter))

    # 2. pop from the max heap, appending the corresponding number of a given letter
    # until the heap is empty
    result = ""
    while max_heap:
        tuple = heappop(max_heap)
        freq = -tuple[0]
        letter = tuple[1]
        for _ in range(freq):
            result += letter

    return result


def main():
    print("String after sorting characters by frequency: " + sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " + sort_character_by_frequency("abcbab"))


main()