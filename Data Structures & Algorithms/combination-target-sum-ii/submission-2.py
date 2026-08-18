class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sols = []

        def dfs(i, sum_so_far):
            if sum_so_far == target:
                res.append(sols[:])
                return
            
            if i >= len(candidates) or sum_so_far > target:
                return

            sols.append(candidates[i])
            dfs(i + 1, sum_so_far + candidates[i])

            sols.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, sum_so_far) 
        
        dfs(0, 0)

        return res