class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_list = list(map(str, nums))
        dct_list = defaultdict(list)
        res = ""
        def compare(x, y):
            if x + y > y + x:
                return -1   
            elif x + y < y + x:
                return 1   
            else:
                return 0
        for c in str_list:
            dct_list[c[0]].append(c)
        
        for i in range(9,-1,-1):
            st = str(i)
            if st in dct_list:
                dct_list[st].sort(key=cmp_to_key(compare))
                res+="".join(dct_list[st])
        
        return str(int(res))
        