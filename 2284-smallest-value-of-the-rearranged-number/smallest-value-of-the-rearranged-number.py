class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            s = sorted(str(num))
            i = 0
            while s[i] == '0':
                i += 1
            s[0], s[i] = s[i], s[0]
            return int("".join(s))
        
        if num < 0:
            s = sorted(str(-num), reverse=True)
            return -int("".join(s))
        
        return 0