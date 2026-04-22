class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        last_op = '+'
        num = 0

        for i, char in enumerate(s): 

            if char.isdigit(): 
                num = num * 10 + int(char)

            if (not char.isdigit() and char != ' ') or i == len(s) - 1:
                # apply last operation 
                if last_op == '-':
                    stack.append(-num)
                elif last_op == '*':
                    stack.append(stack.pop() * num)
                elif last_op == '/':
                    stack.append(int(stack.pop() / num))
                else:
                    stack.append(num)
                num = 0
                last_op = char

        return sum(stack)


        