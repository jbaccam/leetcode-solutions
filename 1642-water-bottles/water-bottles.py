class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = 0 
        DRANK = 0

        while numBottles > 0:
            numBottles -= 1
            emptyBottles += 1
            DRANK += 1

            if emptyBottles == numExchange:
                numBottles += 1
                emptyBottles -= numExchange
        
        return DRANK