class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # (str, open, closed)
        result = []
        stack = [("(", 1, 0)]
        while stack:
            curr, o, c = stack.pop()
            # complete valid string
            if o == c and o == n:
                result.append(curr)
                continue

            # balanced i.e. every open has a closed
            if o == c:
                # adding a open paranthesis
                stack.append((curr+"(", o + 1, c))

            # more open than closed; there will never be more closed than open
            else:
                # if exhausted all open
                if o < n:
                    # adding a open paranthesis
                    stack.append((curr+"(", o + 1, c))
                if c < n:
                    # adding a closed paranthesis
                    stack.append((curr+")", o, c + 1))
        return result






        
        