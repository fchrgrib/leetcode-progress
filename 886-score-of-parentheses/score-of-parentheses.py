class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx = idx_res =  0
        l = len(s)
        bf = -1
        stack = []
        res = [0 for i in range(l)]

        while(idx<l):
            if s[idx] == ')':
                t = stack.pop()
                if bf == -1:
                    res[t] = 1
                elif bf > t:
                    tmp = 0
                    for i in range(bf, t-1,-1):
                        tmp+=res[i]
                        res[i] = 0
                    res[t] = tmp*2
                else:
                    res[t] = 1
                bf = t
            else:
                stack.append(idx)
            idx+=1

        return sum(res)
        