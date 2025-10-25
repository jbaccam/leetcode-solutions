class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        q = deque()
        output = []

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # while smaller values exist in the queue
                q.pop()
            
            # add new value to the queue
            q.append(r)

            # remove the left value from the window because we are sliding
            if l > q[0]: # if left most value is out of bounds of our queue we have to remove that
                q.popleft()

            # have to make sure our window is atleast size k, arrays are 0 index based so + 1 to right and we get the len of the window
            if (r + 1) >= k:
                output.append(nums[q[0]]) # append the maximum, which is the left most value
                l += 1 # left pointer will only be incremented once we have a window of size k
            
            r += 1
        
        return output


