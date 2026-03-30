class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = [] 

        def backtrack(start, current, target): 
            if len(current) == target: 
                self.res.append(current[:])
                return 
            
            remaining_needed = k - len(current)
            for i in range(start, n - remaining_needed + 2):
                current.append(i)
                backtrack(i + 1, current, target)
                current.pop()
        backtrack(1, [], k)
        return self.res
        