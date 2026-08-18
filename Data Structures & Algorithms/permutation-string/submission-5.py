class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False
        
        s1count, s2count = [0] * 26, [0] * 26
        
        for i in range(n1):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
            
        if s1count == s2count: return True
        l = 0
        # Sliding window
        for r in range(n1, n2):
            s2count[ord(s2[r]) - ord('a')] += 1
            s2count[ord(s2[l]) - ord('a')] -= 1
            if s1count == s2count:
                return True
            l+=1
        return False