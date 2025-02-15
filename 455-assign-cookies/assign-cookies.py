class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        l1 = l2 = sum = 0
        g = sorted(g, reverse = True)
        s = sorted(s, reverse = True)

        while(l1<len(g)):
            if l2<len(s) and s[l2] >= g[l1]:
                sum+=1
                l2+=1
            l1+=1

        return sum
        