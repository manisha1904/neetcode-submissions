class MinStack:
    # st = []

    def __init__(self):
        self.st = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.st.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        if not self.st:
            return
        self.st.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if not self.st:
            return -1
        return self.st[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return -1
        return self.min_stack[-1]
        
