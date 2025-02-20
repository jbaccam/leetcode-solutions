# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
# so we know that if theres a bad vers, every vers after that also has to be bad
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result