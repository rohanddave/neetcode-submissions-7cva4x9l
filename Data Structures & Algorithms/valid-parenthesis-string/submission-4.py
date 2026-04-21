class Solution:
    def checkValidString(self, s: str) -> bool:
        max_open, min_open = 0, 0

        for i, char in enumerate(s): 
            if char == '(':
                max_open += 1
                min_open += 1
            elif char == ')':
                max_open -= 1
                min_open -= 1
            else: 
                max_open += 1
                min_open -= 1
            
            if max_open < 0: 
                return False 
            if min_open < 0: 
                min_open = 0

        return min_open == 0       
