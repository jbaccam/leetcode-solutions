class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)

        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles: # this will tell us how many hours each pile took to eat
                hours += math.ceil(p / k) 
                # we need to round up because if it took us 1.1 hours to eat a pile
                # thats 2 hours for the sake of this problem
                # p // k is pile divided by current eating speed = how many hours

            # update the pointers and res depending on the conditions
            if hours <= h:
                res = min(k, res)
                r = k - 1
            else:
                l = k + 1
        
        return res