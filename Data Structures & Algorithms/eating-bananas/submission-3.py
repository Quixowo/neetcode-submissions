class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        res = hi
        while lo <= hi:
            hr = 0
            rate = (lo + hi) // 2
            for pile in piles:
                hr += math.ceil(pile / rate)

            if hr <= h:
                res = min(res, rate)
                hi = rate - 1
            else:
                lo = rate + 1

        return res