class PlateStack:

    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> None:
        if(len(self.st) > 0):
            self.st.pop()

    def top(self) -> int:
        if(len(self.st) == 0):
            return None
        return self.st[-1]

    def getLen(self) -> int:
      return len(self.st)