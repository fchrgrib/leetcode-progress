class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = 0
        n = len(blocks)

        if n < k:
            return res
        
        if n == k:
            for c in blocks:
                if c == "W":
                    res+=1
            return res
        
        res = 2**31
        sum = 0
        i = 0
        for i in range(n):
            if i>= k:
                if blocks[i-k] == "W":
                    sum-=1
            if blocks[i] == "W":
                sum+=1
            if i>= k-1:
                res = min(res, sum)
        print(i)
        return res


        