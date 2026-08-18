class MinStack:

    def __init__(self):
        self.normal = [] # normal list that the user sees
        self.min_stack = [] #behind the scene stack that will make getting the min efficient

    def push(self, val: int) -> None:
        self.normal.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            curr_min = self.min_stack[-1]
            if val < curr_min:
                self.min_stack.append(val)
            else:
                self.min_stack.append(curr_min)

    def pop(self) -> None:
        self.normal.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.normal[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
