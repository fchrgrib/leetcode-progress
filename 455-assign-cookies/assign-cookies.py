class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0

        s.sort()
        g.sort()

        while s and g:
            if s[-1]>=g[-1]:
                res+=1
                s.pop()
                g.pop()
            else:
                g.pop()
        return res
        