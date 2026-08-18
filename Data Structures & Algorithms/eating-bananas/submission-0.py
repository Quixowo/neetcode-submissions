import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        highestER = max(piles)
        lowestER = 1
        res = highestER
        """
        the highest pile in the piles will be the upper bound, 
        (if Koko can eat the biggest pile in bunch in one hour, 
        than it can eat all other piles in one hour too)
        """ 

        while lowestER <= highestER:
            mid = (lowestER + highestER) // 2
            hours = 0
            
            for pile in piles:
                hours += math.ceil(pile/mid)

            if hours <= h:
                res = min(res, mid)
                highestER = mid - 1 
            else:
                lowestER = mid + 1 

        return res