class Solution:
    def calPoints(operations: list[str]) -> int:
        stack = []
        for value in operations:
            if value == 'C':
                stack.pop()
            elif value == 'D':
                stack.append(int(stack[-1]) * 2)
            elif value == '+':
                stack.append(int(stack[-1]) + int(stack[-2]))
            else: stack.append(int(value))
        
        result = 0
        for val in stack:
            result += val
        return result
    

    str = ["5","-2","4","C","D","9","+","+"]
    ans = calPoints(str)
    print(ans)
        