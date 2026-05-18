import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop() 
                if token == '/':
                    stack.append(int(a / b))
                else:
                    stack.append(eval(f"{a}{token}{b}"))
                print(stack)
            else:
                stack.append(int(token))
                print("Appended into stack: ",stack)
        return int(stack[0])