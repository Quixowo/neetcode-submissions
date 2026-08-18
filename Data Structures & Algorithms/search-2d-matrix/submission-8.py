class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            row = (top + bot) // 2
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break

        lo, hi = 0, len(matrix[row]) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return False