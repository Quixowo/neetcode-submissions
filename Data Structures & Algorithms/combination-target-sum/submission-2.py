class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(i, sum_so_far):
            if sum_so_far == target:
                res.append(sol[:])
                return
            if i >= len(nums) or sum_so_far > target:
                return
            
            sol.append(nums[i])
            backtrack(i, sum_so_far + nums[i])

            sol.pop()
            backtrack(i + 1, sum_so_far)
        
        backtrack(0, 0)
        return res