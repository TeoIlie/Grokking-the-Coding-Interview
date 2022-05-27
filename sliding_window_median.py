
class SlidingWindowMedian:

  def find_sliding_window_median(self, nums, k):
    result = []
    sum, windowStart = 0, 0
    for windowEnd in range(len(nums)):
        sum += nums[windowEnd]       
        if windowEnd >= k - 1:
            # at this moment, window holds the correct elements
            print(sum, nums[windowStart], nums[windowEnd])
            sum -= nums[windowStart]
            windowStart += 1

    return result

def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()