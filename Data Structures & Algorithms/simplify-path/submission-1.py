class Solution:
    def simplifyPath(self, path: str) -> str:
        # ['neetcode','practice','','...','','','..','courses']
        p = path.split('/')[1:]
        stack = []
        res = []
        for item in p: 
            if not item or item == '.':
                continue
            if item == '..':
                if stack: 
                    stack.pop()
            else: 
                stack.append(item)
        return '/'+'/'.join(stack)
        