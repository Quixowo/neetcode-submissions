class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0

        for num in nums:
            streak, curr = 1, num
            while (curr + 1) in nums:
                streak += 1
                curr += 1
            res = max(streak, res)
        
        return res


