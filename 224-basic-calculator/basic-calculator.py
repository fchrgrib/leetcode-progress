class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1
        
        stack.append(sign) 
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
                
            elif char in ('+', '-'):
                result += num * sign * stack[-1]
                num = 0
                sign = 1 if char == '+' else -1
                
            elif char == '(':
                stack.append(sign * stack[-1])
                sign = 1
                
            elif char == ')':
                result += num * sign * stack[-1]
                num = 0
                stack.pop()
                sign = 1
                
        if num != 0:
            result += num * sign * stack[-1]
            
        return result