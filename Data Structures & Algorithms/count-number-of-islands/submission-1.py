class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == "1":
                grid[r][c] = "0"
                dfs(r + 1, c)
                dfs(r - 1, c) 
                dfs(r, c + 1) 
                dfs(r, c - 1)
            else:
                return False
            return True

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c):
                    res += 1

        return res
                