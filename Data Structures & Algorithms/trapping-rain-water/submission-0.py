class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        l, r = 0, len(heights) - 1
        maxL = heights[l]
        maxR = heights[r]
        res = 0

        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(heights[l], maxL)
                res += maxL - heights[l]
            else:
                r -= 1
                maxR = max(heights[r], maxR)
                res += maxR - heights[r]
        
        return res
