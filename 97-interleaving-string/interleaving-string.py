class Solution(object):
    def isInterleave(self, s1, s2, s3):
        global l1, l2
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if s1 == s2 == s3 == "":
            return True
        if l1 == 0 or l2 == 0:
            return s1 == s3 or s2 == s3

        if l1 + l2 != l3:
            return False

        global memo
        memo = [[-1 for _ in range(l2+1)] for _ in range(l1+1)]

        def bc(idx1, idx2,idx3, s1, s2, s3):
            global memo
            if idx1 == len(s1) and idx2 == len(s2):
                return True
            if idx1<=len(s1) and idx2<=len(s2) and memo[idx1][idx2] != -1:
                return memo[idx1][idx2]
            
            memo[idx1][idx2] = False

            if idx3< len(s3) and idx1<len(s1) and s3[idx3] == s1[idx1]:
                memo[idx1][idx2] |= bc(idx1+1, idx2, idx3+1, s1, s2, s3)
            if idx3< len(s3) and idx2<len(s2) and s3[idx3] == s2[idx2]:
                memo[idx1][idx2] |= bc(idx1, idx2+1, idx3+1, s1, s2, s3)

            return memo[idx1][idx2]

        return bc(0, 0, 0, s1, s2, s3)