class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        # O(n) time, O(1) space
        max_profit = 0

        # Two pointers
        l = 0
        r = 1

        while r < n:
            if prices[l] <= prices[r]:
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit
                r += 1
            else:
                l += 1
                r = l + 1
        
        return max_profit if max_profit > 0 else 0 