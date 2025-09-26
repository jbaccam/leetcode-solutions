class Solution:
    def trap(self, height: List[int]) -> int:
        # base case if height array is empty
        if not height:
            return 0
        
        # where we are going to accumulate our total amt of water
        output = 0

        # max pointers, start off at first and last index
        maxL = height[0]
        maxR = height[-1]

        # pointers we will be moving
        l = 0
        r = len(height)

        # 

        while l < r:
            if maxL < maxR: # if maxL is less than maxR, we move left pointer
                l += 1
                maxL = max(height[l], maxL) # update the max, if possible
                # the reason we dont have to check for negatives is because we update our max first
                # so maxL will always be equal to or greater than height[l]
                output += maxL - height[l] # update our output based on our current position
            else: 
                r -= 1 # if maxR is greater than maxL, we move right pointer
                maxR = max(height[r], maxR) # update the max, if possible
                output += maxR - height[r] # increement the total
        
        return output
            