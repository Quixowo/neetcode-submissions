class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, canBuy):
            if (i, canBuy) in memo:
                return memo[(i, canBuy)]
            if i >= len(prices):
                return 0

            cooldown = dfs(i + 1, canBuy)
            if canBuy:
                res = dfs(i + 1, not canBuy) - prices[i]
                memo[(i, canBuy)] = max(res, cooldown)
            else:
                res = dfs(i + 2, not canBuy) + prices[i]
                memo[(i, canBuy)] = max(res, cooldown)

            return memo[(i, canBuy)]

        return dfs(0, True)