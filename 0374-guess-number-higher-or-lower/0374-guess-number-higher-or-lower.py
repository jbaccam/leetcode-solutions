# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while True:
            mid = (left + right) // 2
            result = guess(mid)
            if result > 0: # 1 = guess was too low
                left = mid + 1
            elif result < 0: # -1 = guess was too high
                right = mid - 1
            else:
                return mid