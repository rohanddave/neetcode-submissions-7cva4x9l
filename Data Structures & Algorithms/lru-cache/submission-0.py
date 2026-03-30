class Node: 
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = self.nex = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(-1, 0)
        self.right = Node(-1, 0)
        self.left.nex = self.right
        self.right.prev = self.left

    def insert(self, node: Node):
        prev, nex = self.right.prev, self.right
        node.prev = prev
        node.nex = nex
        prev.nex = node
        nex.prev = node

    def remove(self, node: Node):
        prev, nex = node.prev, node.nex
        prev.nex = nex
        nex.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.nex
            self.remove(lru)
            del self.cache[lru.key]
