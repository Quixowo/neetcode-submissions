class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for index, num in enumerate(nums):
            nums_dict[num] = index

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in nums_dict and i != nums_dict[complement]:
                return [i, nums_dict[complement]]
        
        return []