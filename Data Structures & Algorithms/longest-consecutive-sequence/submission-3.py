class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0

        for num in nums:
            curr = num
            length = 1
            if curr - 1 not in nums:
                while curr + 1 in nums:
                    length += 1
                    curr += 1
            
            longest = max(length, longest)
        
        return longest
                