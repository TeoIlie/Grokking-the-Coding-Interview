class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __str__(self) -> str:
    return "[" + str(self.start) + ", " + str(self.end) + "]"

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

  @staticmethod
  def print_intervals(intervals):
    for i,elem in enumerate(intervals):
        elem.print_interval()
        if i != len(intervals) - 1:
            print(', ', end='')
        else:
            print('.')


def merge(intervals):
    merged = []

    # if intervals is length 1, there is nothing to merge
    if len(intervals) == 1:
        return intervals

    # sort intervals by start
    intervals.sort(key=lambda x: x.start)

    # combine intervals as you go
    c = intervals[0]
    for i in range(1,len(intervals)):

        curr_interval = intervals[i]

        # if the current interval overalps the current 'c'
        if curr_interval.start <= c.end:
            c.end = max(c.end, curr_interval.end)
            
        else:
            merged.append(c)
            c = curr_interval
            

    # add what's left after the loop
    merged.append(c)

    return merged


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()

main()