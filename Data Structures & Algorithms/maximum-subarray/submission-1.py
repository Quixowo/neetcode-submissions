class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = curr_max = nums[0]

        for num in nums[1:]:
            curr_max = max(curr_max + num, num)
            global_max = max(global_max, curr_max)
        
        return global_max