class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev_len = 0  # length of previous increasing sequence
        curr_len = 1  # length of current increasing sequence
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_len += 1
            else:
                prev_len = curr_len
                curr_len = 1
            
            # check if we can form two adjacent k-length increasing subarrays
            # either one long streak, or two streaks meeting at a break point.
            if curr_len >= 2*k:
                # one long sequence - can split it: [first k][next k]
                return True
            if prev_len >= k and curr_len >= k:
                # two separate sequences meeting: [last k of prev][first k of curr]
                return True
        
        return False
            