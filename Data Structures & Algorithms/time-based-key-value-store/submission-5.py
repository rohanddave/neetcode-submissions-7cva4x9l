class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap.keys():
            self.hashmap[key].append((value, timestamp))
        else:
            self.hashmap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap.keys():
            return ""
        arr = self.hashmap[key]
        l, r = 0, len(arr) - 1
        res = ""
        while l <= r: 
            m = (l + r) // 2
            value, t = arr[m]
            if t <= timestamp:
                l = m + 1
                res = value
            elif timestamp < t:
                r = m - 1
        return res