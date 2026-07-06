class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # O(n) time, O(n) space
        # Get postfix maxes using concurrent updater
        post_maxes = [0] * len(prices)
        curr_max = 0

        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > curr_max:
                curr_max = prices[i]
            post_maxes[i] = curr_max
        
        # Compute the potential profits
        profits = []

        for i in range(len(prices)):
            profit = post_maxes[i] - prices[i]
            profits.append(profit)
        
        return max(profits)
