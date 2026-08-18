class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sums = []

        def dfs(i, sum_so_far):
            if sum_so_far == target:
                res.append(sums[:])
                return

            if i >= len(nums) or sum_so_far > target:
                return

            #don't slice nums
            sums.append(nums[i])
            dfs(i, sum_so_far + nums[i])

            #slice nums
            sums.pop()
            dfs(i + 1, sum_so_far)

        dfs(0, 0)

        return res