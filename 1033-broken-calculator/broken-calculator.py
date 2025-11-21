class Solution:
    def brokenCalc(self, s: int, t: int) -> int:
        step = 0

        while t>s:
            if t%2 == 0:
                t = int(t/2)
            else:
                t+=1
            step+=1
        return step + (s-t)

        