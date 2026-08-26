class MinStack:

    def __init__(self):
        self.main = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.main.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)
        

    def pop(self) -> None:
        removed = self.main.pop()
        if removed == self.min[-1]:
            self.min.pop()
        

    def top(self) -> int:
        return self.main[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        
