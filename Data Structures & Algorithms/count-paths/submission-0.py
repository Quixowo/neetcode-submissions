class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}  # (row, column) -> number of unique ways

        def dfs(r, c):
            if r >= m or c >= n:
                return 0
            if r + 1 == m and c + 1 == n:
                return 1
            if (r, c) in memo:
                return memo[(r, c)]
            else:
                res = dfs(r + 1, c) + dfs(r, c + 1)
                memo[(r, c)] = res

            return memo[(r, c)]

        return dfs(0, 0)