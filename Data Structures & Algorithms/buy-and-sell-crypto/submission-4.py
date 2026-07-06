class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Store postfix maxes
        post_maxes = []

        # Obtain postfix maxes
        for i in range(len(prices)):
            post_maxes.append(max(prices[i:]))

        # Get possible profits
        profits = []
        
        for i in range(len(prices)):
            profits.append(post_maxes[i] - prices[i])

        # Find maximum profit
        best_profit = max(profits)
    
        return best_profit
        