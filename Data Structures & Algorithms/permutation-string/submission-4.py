class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0

        for r in range(len(s1), len(s2)+1):
            if sorted(s1) == sorted(s2[l:r]):
                return True
            l += 1
        return False