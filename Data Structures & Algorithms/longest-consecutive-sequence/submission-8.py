class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_so_far = 0

        for i in range(len(nums)):
            curr = nums[i]
            if curr - 1 not in nums:
                length = 1
                while (curr + length) in set_nums:
                    length += 1
                max_so_far = max(max_so_far, length)


        return max_so_far        