class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in tracker:
                return [tracker[difference], i]
            tracker[n] = i
        