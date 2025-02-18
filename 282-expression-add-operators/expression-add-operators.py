class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        global res
        res = []
        if int(num) == target and int(num)>0:
            return [num]

        def bc(idx, num, target, step):
            global res
            # print(step)
            if idx == len(num)-1:
                if target == eval(step):
                    res.append(step)
                return
            c = ""
            for i in range(idx+1,len(num)):
                if len(c)> 0 and c[0] == "0":
                    break
                c+=num[i]
                tmp = step+"*"+c
                bc(i, num, target, tmp)
                tmp = step+"+"+c
                bc(i, num, target, tmp)
                tmp = step+"-"+c
                bc(i, num, target, tmp)
                

        c = ""
        for i in range(0, len(num)-1):
            if len(c)> 0 and c[0] == "0":
                    break
            c+=num[i]
            bc(i, num, target, c)

        
        return res