class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_so_far = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                max_so_far = max(max_so_far, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return max_so_far
                