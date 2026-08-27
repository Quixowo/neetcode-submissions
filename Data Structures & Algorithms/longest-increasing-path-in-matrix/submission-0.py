class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = {} # (x, y) -> longest stricttly increasing path stored
        
        def dfs(x, y):
            if (x, y) in memo:
                return memo[(x, y)]

            res = 1
            curr = matrix[x][y]
            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] > matrix[x][y]:
                    res = max(res, 1 + dfs(nx, ny))
            
            memo[(x, y)] = res

            return memo[(x, y)]

        sol = 1
        for x in range(rows):
            for y in range(cols):
                sol = max(sol, dfs(x, y))

        return sol