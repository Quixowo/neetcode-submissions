class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = [[-1] * 2 for _ in range(len(nums))]
        
        def dfs(i, firstIsRobbed):
            if i >= len(nums) or (firstIsRobbed and i == len(nums) - 1):
                return 0
            if memo[i][firstIsRobbed] != -1:
                return memo[i][firstIsRobbed]

            memo[i][firstIsRobbed] = max(dfs(i + 1, firstIsRobbed), nums[i] + dfs(i + 2, firstIsRobbed))
            return memo[i][firstIsRobbed]

        return max(dfs(0, True), dfs(1, False))