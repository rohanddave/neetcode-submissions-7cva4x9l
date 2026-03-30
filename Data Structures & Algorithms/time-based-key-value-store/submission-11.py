from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((value, timestamp))        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m: 
            print('returning because key not in map')
            return "" 
        
        values = self.m[key]
        l, r = 0, len(values)
        while l < r: 
            m = (l + r) // 2
            if values[m][1] > timestamp:
                r = m
            else:
                l = m + 1
        
        return "" if l == 0 else values[l - 1][0]
