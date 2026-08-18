class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        brackets = {'(' : ')',
                    '{' : '}',
                    '[' : ']'}
        stack = []

        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if not stack or brackets[stack.pop()] != c:
                    return False
        
        return not stack 



