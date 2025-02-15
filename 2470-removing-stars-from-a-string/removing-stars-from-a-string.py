class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        idx = sum = 0
        while idx < len(s):
            if s[idx] == '*':
                sum +=1
            if sum != 0 and (s[idx] != '*' or idx == len(s)-1) :
                tmp = len(s)
                if s[idx] == '*':
                    s = s[0:idx-2*sum+1] + s[idx+1 : len(s)]
                else:
                    s = s[0:idx-2*sum] + s[idx : len(s)]
                
                if 2*sum >idx:
                    s = ""
                if idx == tmp - 1:
                    idx+=1
                else:
                    idx = idx - 2*sum
                sum = 0
                # print(idx)
            idx+=1
        return s
        