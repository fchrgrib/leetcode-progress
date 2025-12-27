class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], t: int) -> int:
        c = len(mat[0])
        r = len(mat)
        dp = {}
        if c == 1:
            for i in mat:
                t-=i[0]
            return abs(t)

        def dfs(row, target):
            nonlocal r, mat, dp,t
            if (row, target) in dp:
                return dp[(row, target)]
            if row>r-1:
                return float("inf")
            tmp_t= set()
            tmp_r = []
            if row == r-1:
                tmp = [abs(target-i) for i in mat[row]]
                return min(tmp)
            for i in mat[row]:
                if target-i in tmp_t:
                    continue
                if target-i <0 and abs(target-i)>70*3:
                    continue
                tmp_r.append(dfs(row+1, target-i))
                tmp_t.add(target-i)
            if tmp_r:
                dp[(row, target)] = min(tmp_r)
                return dp[(row, target)]
            return float("inf")
        
        return dfs(0, t)