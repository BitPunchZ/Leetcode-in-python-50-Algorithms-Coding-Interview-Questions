class MinStack:
    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        curMin = self.getMin()
        if curMin == None or curMin > x:
            curMin = x
        self.st.append((x, curMin))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0] if self.st else None

    def getMin(self) -> int:
        return self.st[-1][1] if self.st else None
