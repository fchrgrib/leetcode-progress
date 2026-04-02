class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ln1, ln2 = len(s), len(p)
        if ln1 == ln2 == 0:
            return True
        if ln1 == 0:
            chrc = list(set(list(p)))
            return len(chrc) == 1 and chrc[0] == "*"

        dp = {}

        def backtrack(idx1, idx2):
            store = (idx1, idx2)
            if store in dp:
                return dp[store]
            if idx1 == ln1 and idx2 == ln2:
                return True
            if idx2 == ln2-1 and p[idx2] == "*":
                return True
            if idx2 >= ln2:
                return False
            if idx1 < ln1 and s[idx1] != p[idx2] and p[idx2] != "*" and p[idx2] != "?":
                return False

            dp[store] = False
            if idx1<ln1 and (s[idx1] == p[idx2] or p[idx2] == "?"):
                dp[store] = backtrack(idx1+1, idx2+1)
                return dp[store]
            
            for i in range(idx1, ln1+1):
                while idx2<ln2 and p[idx2] == "*":
                    idx2+=1
                dp[store] |= backtrack(i,idx2)
            return dp[store]


        return backtrack(0,0)
        