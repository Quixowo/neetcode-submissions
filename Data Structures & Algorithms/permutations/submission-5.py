class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        bools = [False] * len(nums)
        def dfs(cur, bools):
            if all(bools):
                res.append(cur.copy())
                cur = []
                return

            for i in range(len(nums)):
                if bools[i] == False:
                    cur.append(nums[i])
                    bools[i] = True
                    dfs(cur, bools)

                    cur.pop()
                    bools[i] = False

        dfs([], bools)
        return res