class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]
        l = 0
        r = len(nums) -1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]: 
            # we know that this is sorted left - mid, so the left val would be the smallest
            # and we already compared and checked it against mid since res is initalized as the left pointer
            # now we can check the other vals on the right
                l = m + 1
            else: # the mid is less than the values on the left
                r = m - 1
        
        return res

        