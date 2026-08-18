class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        brackets = {']': '[',
                    '}': '{',
                    ')': '('}

        stack = []

        for bracket in s:
            if bracket in brackets:
                if stack and stack[-1] == brackets[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return True if not stack else False
                 