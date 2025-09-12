class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # so we want to find two different index's where the numbers are the same
        # and where the indices absolute value of i - j is less than or equal to k
        # k pretty much means that these integers must within k positions
        # so like if we have k = 2, the matching integers must be within 2 positions of eachother

        # i think what we could do is use a sliding window of k size, and check in this window if duplicates exist
        # this will meat the conditions that they are the same numbers and also within k 
        # and to check if theres duplicates, when moving the window we can keep track of the numbers in the window using a set, so we can have o(1) lookup

        window = set()

        l = 0
        for r in range(len(nums)):
            # if the number we just added already exists in the set
            if nums[r] in window:
                return True
            
            # if the value doesnt already exist, we need to add it
            window.add(nums[r])

            # if our window becomes greater than k, we must move the left pointer to the right once
            # and then remove that value from our set, making our window slide
            if len(window) > k:
                window.remove(nums[l])
                l += 1
        
        # it will break out of the for loop if the window reaches the end of array and doesnt find a match
        return False
