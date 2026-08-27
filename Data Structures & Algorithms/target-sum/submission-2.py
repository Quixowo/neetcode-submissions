class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} # key (index, curr_sum), value is cached total ways

        def dfs(i, curr_sum):
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            if i == len(nums) and curr_sum == target:
                return 1
            if i >= len(nums):
                return 0
            
            res = dfs(i + 1, curr_sum + (-nums[i])) + dfs(i + 1, curr_sum + nums[i])
            memo[(i, curr_sum)] = res

            return memo[(i, curr_sum)]

        return dfs(0, 0)

