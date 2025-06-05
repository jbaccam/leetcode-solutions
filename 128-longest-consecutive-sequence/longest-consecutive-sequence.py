class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # check if this is the start of a sequence
            if (num-1) not in numSet:
                length = 0
                while (num+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    #  |1 2 3 4 | 100 | 200 |
    # <--------------------->
    #  |    4   |   1 |  1 |