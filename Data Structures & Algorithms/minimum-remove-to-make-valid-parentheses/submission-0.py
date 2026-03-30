class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # valid strings = ['aa','','(a)','aa(a)','a','aa(a)a']
        # valid strings without paranthesis = ['aa','a','']
        stack = [] 
        idx = set()
        for i,char in enumerate(s): 
            if char == '(':
                stack.append(i)
            elif char == ')': 
                if stack:
                    stack.pop()
                else:
                    idx.add(i)
        
        idx.update(stack)

        return ''.join(char for i, char in enumerate(s) if i not in idx)
        