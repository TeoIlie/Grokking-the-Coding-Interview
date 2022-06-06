def search_next_letter(letters, key):
    # TODO: Write your code here
    start, end = 0, len(letters) - 1
    if key >= letters[-1]:
        return letters[0]
    while start <= end:
        middle = (start + end)//2
        if letters[middle] == key:
            return letters[middle + 1]
        if key < letters[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return letters[start]



def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'h'))


main()