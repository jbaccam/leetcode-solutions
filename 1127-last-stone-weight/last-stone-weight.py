class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # invert all the values to make a max heap
        heapq.heapify(stones) # heapify the array

        # while its > 1, 1 because there can be 1 stone remaining, if 2 stones collide they can make 0 or 1 
        while len(stones) > 1:
             first = heapq.heappop(stones)  
             second = heapq.heappop(stones)    
             if second > first: # cuz our nums our negative, if second was -7 and first was -8, second would be greater
                                # but in reality, first would be, its just for the condition
                # heapq.heappush(stones, second - first) this would be like -7 - -8 which is -7 + 8 which gets us what we want
                # but we dont actually want that cause we want the negative values in our heap so we just do
                heapq.heappush(stones, first - second) # this gives us the negative difference

        stones.append(0) # make sure its not empty, if theres no stones than it will be 0, if there is, then this will just do nothing
        return abs(stones[0]) # want the positive value
