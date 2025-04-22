class Solution:
    def camelMatch(self, q: List[str], p: str) -> List[bool]:
        n = len(q)
        res = [False for _ in range(n)]

        def is_match(l1, l2):
            i1 = i2 = 0

            n1 = len(l1)
            n2 = len(l2)

            while i1 < n1:
                if i2 < n2 and l1[i1] == l2[i2]:
                    i2+=1
                    i1+=1
                    continue
                if i2>=n2 and l1[i1].isupper():
                    return False
                if l1[i1].isupper():
                    i2 = 0
                i1+=1
            
            return i2 >= n2
        
        for i in range(n):
            res[i] = is_match(q[i], p)
        return res
        