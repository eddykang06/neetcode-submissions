class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        # O(n) time, O(1) space
        curr_max = 0
        profit_max = 0

        for i in range(n-1, 0, -1):

            # Update the post fix max
            if prices[i] > curr_max:
                curr_max = prices[i]
            
            # Compute the current profit and update max if needed
            profit = curr_max - prices[i-1]
            
            if profit > profit_max:
                profit_max = profit
        
        return profit_max