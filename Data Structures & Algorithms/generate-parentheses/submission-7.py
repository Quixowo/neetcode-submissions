class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, close, sols):
            if (open > n) or (close > open):
                return
            
            if (open + close) == (2 * n):
                res.append(sols[:])
                return

            dfs(open + 1, close, sols + '(')

            dfs(open, close + 1, sols + ')')

        dfs(0, 0, "")
        return res
