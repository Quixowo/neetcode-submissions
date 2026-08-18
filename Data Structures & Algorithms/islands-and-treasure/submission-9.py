class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] #left, up, right, down
        queue = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            curr_r, curr_c = queue.popleft()
            for dr, dc in directions:
                nr, nc =  curr_r + dr, curr_c + dc 
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[curr_r][curr_c] + 1
                    queue.append((nr, nc))