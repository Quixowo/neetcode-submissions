class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        half_sum = sum(nums) / 2
        memo = {}
        
        def dfs(i, curr_sum):
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            
            if curr_sum == half_sum:
                return True
            if i >= len(nums) or curr_sum < 0:
                return False

            if dfs(i + 1, curr_sum + nums[i]):
                memo[(i, curr_sum)] = True
            else:
                memo[(i, curr_sum)] = dfs(i + 1, curr_sum)

            return memo[((i, curr_sum))]

        return dfs(0, 0)
            