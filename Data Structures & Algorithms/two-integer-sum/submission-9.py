class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_nums = {}

        for index, num in enumerate(nums):
            index_nums[num] = index

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums and index_nums[complement] != i:
                return [i, index_nums[complement]]