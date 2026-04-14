class Solution:
    def calculate(self, s: str) -> int:
        stack = [1]
        sign = 1
        num = 0
        res = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            elif c in '+-':
                res += sign * stack[-1] * num
                num = 0
                sign = 1 if c == '+' else -1

            elif c == '(':
                stack.append(stack[-1] * sign)
                sign = 1

            elif c == ')':
                res += sign * stack[-1] * num
                num = 0
                stack.pop()

        return res + sign * stack[-1] * num