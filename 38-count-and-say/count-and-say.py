class Solution:
    def countAndSay(self, n: int) -> str:

        def rle(n):
            sum = 0
            init = n[0]
            s = ""

            for i in range(len(n)+1):
                if i == len(n) or init != n[i]:
                    s+=f"{sum}{init}"
                    sum = 1
                    if i<len(n):
                        init = n[i]
                    continue
                sum+=1
            return s
        
        s = ""
        for i in range(n):
            if i == 0:
                s = "1"
                continue
            
            s = rle(s)
        return s
                
        