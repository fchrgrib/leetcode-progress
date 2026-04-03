class Solution:
    def smallestNumber(self, num: int) -> int:
        if num>0:
            get_str = sorted(list(str(num)))
            idx = 0
            while idx<len(get_str) and get_str[idx] == "0":
                idx+=1
            if idx!=0:
                get_str[0], get_str[idx] = get_str[idx], get_str[0]
            return int("".join(get_str))
        elif num<0:
            get_str = sorted(list(str(num)[1:]), reverse=True)
            return -1*int("".join(get_str))
        return 0
        