class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {')':'(', '}': '{', ']': '['}

        for char in s: 
            if char in m.values():
                stack.append(char) 
            else: 
                if not stack or stack[-1] != m[char]:
                    return False
                stack.pop()
        
        return len(stack) == 0
        