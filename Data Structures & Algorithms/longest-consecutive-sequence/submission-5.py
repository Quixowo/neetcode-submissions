class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in nums:
                length = 1
                while num + length in nums:
                    length += 1
            
                longest = max(length, longest)
        
        return longest
                