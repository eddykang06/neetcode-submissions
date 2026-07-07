class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Two pointers
        l = 0
        r = 1

        # max profit
        max_profit = 0

        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            max_profit = max(curr_profit, max_profit)

            if prices[l] < prices[r]:
                r += 1
                
            else:
                l = r
                r = l + 1
        
        return max_profit
        