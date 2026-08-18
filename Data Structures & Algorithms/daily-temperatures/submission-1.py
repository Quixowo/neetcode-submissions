class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stack_index, stack_temperature = stack.pop()
                res[stack_index] = i - stack_index
            stack.append((i, temp))

        return res