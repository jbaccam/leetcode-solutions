class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        k = 0 # track the longest k
        prevlen = 0 # length of the previous strictly increasing subarray
        # [2,5,7,8,9,2,3,4,3,1]
        # prevlen would be 2,5,7,8,9
        # we dont continue because the 2 is no longer increasing 
        # but we need to track the length of two adject arrays
        currlen = 1 # length of the current strictly increasing subarray
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                # increment the current increasing array 
                currlen += 1
            else:
                # save currlen to prevlen before resetting currlen
                prevlen = currlen
                currlen = 1

            # currlen // 2 just incase theres an array that is always increasing
            # then we can just divide it by 2 to get the max k size adjacent increasing subararys
            # and then we take the max of k, the min between currlen and prevlen, like in the example, 
            # we are bottlenecked by the smallest, k must be the same size for both of them
            # and currlen as a last check
            k = max(k, min(currlen,prevlen), currlen //2)
        
        return k


