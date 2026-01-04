class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        dp = {}
        if l1 == l2 == l3 == 0:
            return True

        if l1+l2 != l3:
            return False

        def recurs(i1, i2, i3):
            nonlocal l1,l2,l3,s1,s2,s3, dp
            store = ((i1, i2), i3)

            if i3 == l3:
                return True
            if store in dp:
                return dp[store]
            

            dp[store] = False
            next_i1, next_i2 = i1+1, i2+1

            if i1 < l1 and s1[i1] == s3[i3]:
                dp[store] |= recurs(next_i1, i2, i3+1)
            if i2 < l2 and s2[i2] == s3[i3]:
                dp[store] |= recurs(i1, next_i2, i3+1)
            return dp[store]
        
        return recurs(0,0,0)
        