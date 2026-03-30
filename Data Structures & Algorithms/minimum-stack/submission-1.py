import sys
class MinStack:
    def __init__(self):
        self.minStack = []
        self.arr = []
        self.topIndex = -1

    def push(self, val: int) -> None:
        self.arr.append(val)  
        minValue = min(self.getMin(), val)
        self.topIndex += 1
        self.minStack.append(minValue)

    def pop(self) -> None:
        if self.topIndex >= 0:
            self.topIndex -= 1
            self.arr.pop()
            self.minStack.pop()

    def top(self) -> int:
        return self.arr[self.topIndex]
        

    def getMin(self) -> int:
        return sys.maxsize if self.topIndex == -1 else self.minStack[self.topIndex]

        
