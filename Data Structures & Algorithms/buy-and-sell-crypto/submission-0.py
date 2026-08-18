class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
    
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                profit = sell - buy
                res = max(res, profit)
        return res
