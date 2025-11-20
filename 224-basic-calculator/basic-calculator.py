class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        def sum_number(s: str) -> int:
            # print(s)
            
            sm = tmp = 0
            is_m = 1

            for i in range(len(s)):
                if s[i] == "+" or s[i] == "-":
                    sm += (is_m * tmp)
                    tmp = 0
                    if s[i] == "+":
                        is_m = 1
                    else:
                        if i>0 and s[i-1] == "-":
                            is_m*=-1
                        else:
                            is_m = -1
                    continue
                if s[i].isspace():
                    continue
                tmp = (tmp * 10) + int(s[i])
                    
            return sm + (is_m * tmp)
        
        stack = []
        i = 0
        l = len(s)
        while i<l:
            if s[i] == "(":
                stack.append(i)
            if s[i] == ")":
                tmp_idx = stack.pop()
                start = tmp_idx+1
                end = start+ (i-(start))
                tmp_res = sum_number(s[start:end])
                s = s[:tmp_idx] + str(tmp_res) + s[i+1:]
                # print(s)
                # print(s)
                i = len(s[:tmp_idx] + str(tmp_res)) -1
                # print("index: ",i)
                l = len(s)
            i+=1
        # print(s)
        
        return sum_number(s)
                        


        