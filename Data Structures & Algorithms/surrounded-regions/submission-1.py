class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        unsurrounded = set()

        # dfs that takes in a circle and does a search for its area
        def dfs(r, c, visited_set):
            if (r < 0 or r == rows or 
            c < 0 or c == cols or 
            (r, c) in visited_set or 
            board[r][c] == "X"):
                return
            
            visited_set.add((r, c))
            dfs(r + 1, c, visited_set)
            dfs(r - 1, c, visited_set)
            dfs(r, c + 1, visited_set)
            dfs(r, c - 1, visited_set)
            
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0, unsurrounded)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1, unsurrounded)
        
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c, unsurrounded)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c, unsurrounded)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in unsurrounded:
                    board[r][c] = "X"
        
