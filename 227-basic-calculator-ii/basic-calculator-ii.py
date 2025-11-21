class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        res = 0
        last_num = 0
        last_op = '+'
        
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            
            if c in "+-*/" or i == len(s) - 1:
                if last_op == '+':
                    res += last_num
                    last_num = num
                elif last_op == '-':
                    res += last_num
                    last_num = -num
                elif last_op == '*':
                    last_num = last_num * num
                elif last_op == '/':
                    last_num = int(last_num / num)
                
                last_op = c
                num = 0
        
        res += last_num
        return res