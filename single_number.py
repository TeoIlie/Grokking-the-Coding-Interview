def find_single_number(arr):
    num = arr[0]
    for i in range(1,len(arr)):
        num ^= arr[i]
    return num

def main():
    arr = [1, 5, 2, 1, 3, 2, 3, 5, 6]
    print(find_single_number(arr))

main()