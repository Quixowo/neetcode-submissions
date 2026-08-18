class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ""

        window, countT = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)   

            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                #remove from left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l:r + 1] if resLen != float('inf') else ''