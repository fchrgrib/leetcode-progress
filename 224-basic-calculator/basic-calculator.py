class Solution:
    def calculate(self, s: str) -> int:
        signs = [1]
        sign = 1
        num, res = 0, 0

        for c in s:

            if c.isdigit():
                num = num*10+int(c)
            
            if c == "(":
                signs.append(sign*signs[-1])
                sign = 1
            if c == ")":
                res+=(num*(sign*signs[-1]))
                num = 0
                signs.pop()
            

            if c in "+-":
                res+=(num*(sign*signs[-1]))
                if c == "+":
                    sign = 1
                else:
                    sign = -1
                num = 0
        return res + (sign*signs[-1])*num
                
