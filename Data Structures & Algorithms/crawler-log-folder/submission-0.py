class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for char in logs: 
            if char == './':
                continue 
            if char == '../':
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return len(stack)