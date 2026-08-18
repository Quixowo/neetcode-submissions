class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False #edge case
        
        copy_s = sorted(s)
        copy_t = sorted(t)

        for i in range(len(s)):
            if not copy_s[i] == copy_t[i]:
                return False
        return True