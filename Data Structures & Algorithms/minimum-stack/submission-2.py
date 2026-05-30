class MinStack:
    # st = []

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        self.st.append(val)

    def pop(self) -> None:
        if not self.st:
            return
        self.st.pop()

    def top(self) -> int:
        if not self.st:
            return -1
        return self.st[-1]

    def getMin(self) -> int:
        min_val = float('inf')
        for val in self.st:
            min_val = min(min_val, val)
        return min_val
        
