class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for index, value in enumerate(nums):
            nums_dict[value] = index
        
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in nums_dict and nums_dict[complement] != i:
                return [i, nums_dict[complement]]

        return []