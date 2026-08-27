class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == len(s1) and j == len(s2):
                return True

            k = i + j
            res = False
            if i < len(s1) and s3[k] == s1[i] and dfs(i + 1, j):
                res = True
            if not res and j < len(s2) and s3[k] == s2[j] and dfs(i, j + 1):
                res = True
            
            memo[(i, j)] = res

            return memo[(i, j)]

        return dfs(0, 0)