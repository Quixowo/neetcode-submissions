class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #search vertically first, then search horizontally
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        low, high = 0, len(matrix[0]) - 1
        
        while low <= high:
            mid = (low + high) // 2

            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        return False 
