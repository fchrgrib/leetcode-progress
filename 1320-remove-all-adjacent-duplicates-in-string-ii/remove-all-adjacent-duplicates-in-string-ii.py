class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = ""
        stack = []
        for i in range(len(s)):
            if i == 0:
                res+=s[i]
                stack.append([s[0], 1])
                continue
            if stack and stack[-1][0] == s[i]:
                stack[-1][1]+=1
            else:
                stack.append([s[i], 1])
            res+=s[i]
            
            if stack[-1][1] == k:
                stack.pop()
                ls = len(res)
                res = res[:ls-k]
        return res

        