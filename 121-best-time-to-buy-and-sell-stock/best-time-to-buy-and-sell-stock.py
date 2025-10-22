class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        left = 0
        right = 1
        while right < len(prices):
            curr_profit = prices[right] - prices[left] # sell - buy = profit 
            max_profit = max(curr_profit, max_profit) # check if we found a new profit

            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                right += 1
        
        return max_profit