from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #If you check for len() == 1 and early return, save memory; compromise runtime.
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                stack.append((stack.pop() - stack.pop()) * -1 )
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                stack.append(int((1/stack.pop())* stack.pop()))
            else:
                stack.append(int(token))
        return stack[0]