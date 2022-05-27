def find_happy_number(num):
    # this problem maps to finding a cycle in the linked list
    # one approach is to store all previously encountered numbers,
    # and find the cycle that way, but that requires extra storage
    # instead we solve this using slow,fast pointer, where finding the same
    # number is a 'cycle', and finding 1 is like finding 'Null'
    point1, point2 = num, num
    while point2 != 1 and get_next_num(point2) != 1:
        point1 = get_next_num(point1)
        point2 = get_next_num(get_next_num(point2))
        if point1 == point2:
            return False
    return True


def get_next_num(n):
    digits = []
    while n >= 9:
        digits.append(n % 10)
        n = n // 10
    digits.append(n)
    sum_squares = 0
    for elem in digits:
        sum_squares += elem ** 2
    
    return sum_squares


def main():
    print('\nIs 23 happy? ', end='')
    print('Answer', find_happy_number(23))
    print('\nIs 12 happy? ', end='')
    print('Answer', find_happy_number(12))


main()