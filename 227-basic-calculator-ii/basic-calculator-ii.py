class Solution:
    def calculate(self, s: str) -> int:
        sign = 1
        num = res = 0
        symb = []
        md = []

        def md_res(md, symb, num):
            if len(md) == 0:
                return 0
            
            res = md[0]
            for i in range(len(md)):
                if i < len(md)-1:
                    tmp_next = md[i+1]
                else:
                    tmp_next = num
                
                if symb[i] == "*":
                    res*=tmp_next
                else:
                    res=int(res/tmp_next)
            return res



        for c in s:
            # print(res)
            if c.isspace():
                continue
            
            if c == "+" or c == "-":
                num*=sign
                sign = 1 if c == "+" else -1
                if len(md)>0:
                    res+= md_res(md, symb, num)
                    # print(md)
                    # print(res)
                    md.clear()
                    symb.clear()
                else:
                    res+=num
                num = 0
                continue
            if c == "*" or c=="/":
                md.append(num*sign)
                symb.append(c)
                num = 0
                sign = 1
                continue
            num = num*10 + int(c)
        
        if len(md)>0:
            res+= md_res(md, symb, num)
            # print(md)
            md.clear()
            symb.clear()
            num = 0
            # print(res)
        if num != 0:
            res+=(sign*num)
        # print(res)
        return res
                
                