class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {} # key (i, j), indexes of s and t respectively, value is the num distincts from those two indexes

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == len(s) and j < len(t):
                return 0
            
            # able to successfully reach the end of t, so a succesful solution was found
            if j == len(t):
                return 1

            res = 0
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            
            res += dfs(i + 1, j)

            memo[(i, j)] = res

            return memo[(i, j)]

        return dfs(0, 0)
