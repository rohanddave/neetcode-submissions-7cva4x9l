class MinStack:

    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:
        curr_min = min(val, self.stack[-1][1] if self.stack else float('inf'))
        self.stack.append((val, curr_min))
        

    def pop(self) -> None:
        return self.stack.pop()[0]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
