class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sols = []

        def dfs(i):
            if i >= len(s):
                res.append(sols[:])
            
            for j in range(i, len(s)):
                if self.isPalindrome(s[i : j+1]):
                    sols.append(s[i : j+1])
                    dfs(j + 1)      
                    sols.pop()
        
        dfs(0)
        return res

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True