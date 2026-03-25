class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ln = len(triangle)
        if ln == 1:
            return min(triangle[0])
        dp = {}
        dp[(0,0)] = triangle[0][0]
        res = float("inf")

        for i in range(1,ln):
            for j in range(len(triangle[i])):
                curr_num = triangle[i][j]
                dp[(i,j)] = min(dp.get((i-1,j-1), float("inf")) + curr_num, dp.get((i-1,j), float("inf")) + curr_num)

                if i == ln-1:
                    res = min(res, dp[(i,j)])
        return res
        