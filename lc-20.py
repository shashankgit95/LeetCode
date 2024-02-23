class Solution:
    #Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    def isValid(s: str) -> bool:
        stack = []
        stack.append('/')
        for ch in s:
            match ch:
                case '(':
                    stack.append(ch)
                case '[':
                    stack.append(ch)
                case '{':
                    stack.append(ch)
                case ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else: return False
                case ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else: return False
                case '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else: return False
        return stack.pop() == '/'
    

    s = '('
    print(isValid(s))