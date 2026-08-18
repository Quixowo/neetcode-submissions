class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for letter in s:
            countS[letter] = 1 + countS.get(letter, 0)
        
        for letter in t:
            countT[letter] = 1 + countT.get(letter, 0)

        return countS == countT