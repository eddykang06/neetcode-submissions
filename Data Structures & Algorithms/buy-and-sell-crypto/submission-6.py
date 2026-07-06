class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # O(n^2), O(1)
        res = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > res:
                    res = prices[j] - prices[i]
        
        return res
