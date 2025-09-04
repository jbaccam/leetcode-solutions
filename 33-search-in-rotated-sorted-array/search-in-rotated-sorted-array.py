class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initalize our pointers like a typical binary search
        left = 0 
        right = len(nums) - 1

        while left <= right: 
            mid = (left+right) // 2

            if target == nums[mid]:
                return mid

            # IF the mid pointer number is larger than the left pointer number,
            # then we KNOW that from the left pointer, to the right pointer, IS SORTED
            if nums[mid] >= nums[left]: 
            # but how can we tell if our value is in this part of the sorted array?
            # first we can check, if our value is LESS than the number at the position of the left pointer
            # then it is NOWHERE in between the left and the middle pointer. OR if the target is greater than the midpoint
            # we know it CANNOT be anywhere to the left of the midpoint since it is sorted in ascending order
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
            # this else is for if the midpoint is LESS than left pointer, we know that from the midpoint to the right
            # is sorted in ascending order. SO, we can check, if our target is less than the midpoint,
            # it CANNOT be in the right side, and if it greater than the right side, it CANNOT be in the right side
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        # if we never find the target return -1, cuz this binary search will return rearly if it finds the target, if it runs
        # through all the numbers to get here, then it didnt find the target
        return -1
