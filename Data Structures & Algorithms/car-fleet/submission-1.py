class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(pos, speed) for pos, speed in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for pos, speed in pairs:
            time = (target - pos) / speed
            if not stack or stack[-1][2] < time:
                stack.append((pos, speed, time))
            
        return len(stack)
