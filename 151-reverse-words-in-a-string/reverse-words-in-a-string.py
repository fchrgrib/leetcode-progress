class Solution:
    def reverseWords(self, s: str) -> str:
        res = temp = ""
        n = len(s)
        sp = 0


        for i in range(n):
            if s[i] != " ":
                sp = 0
            else:
                sp += 1
            
            if sp>1:
                continue
            temp+=s[i]
        
        if temp[0] == " ":
            temp = temp[1:]
        n = len(temp)
        if temp[n-1] == " ":
            temp = temp[:n-1]
        n = len(temp)

        t = temp.split(" ")
        for i in range(len(t)-1, -1, -1):
            res+=(t[i]+" ")

        return res[:len(res)-1]
        
        