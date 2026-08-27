class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {} # holds (i, j) indices of word1 and word2 -> min transformations from those indices onward
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(word1):
                return len(word2) - j
            # successfully reached end of word2
            if j == len(word2):
                return len(word1) - i
            
            #deletion: dfs(i + 1, j), skip an index in word1, simulating deletion
            #replacement: dfs(i + 1, j + 1) move forward as if there was a match
            #insertion: dfs(i, j + 1) added extra character to i, meaning the index stays the same

            if word1[i] != word2[j]:
                res = 1 + min(dfs(i + 1, j), dfs(i + 1, j + 1), dfs(i, j + 1))
            else:
                res = dfs(i + 1, j + 1)

            memo[(i, j)] = res
            return memo[(i, j)]

        return dfs(0, 0)
            

            