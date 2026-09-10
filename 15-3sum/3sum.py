class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) -1
            while left < right:
                value = n + nums[left] + nums[right]
                if value > 0: 
                    right -= 1
                elif value < 0:
                    left += 1
                else:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        
        return res
