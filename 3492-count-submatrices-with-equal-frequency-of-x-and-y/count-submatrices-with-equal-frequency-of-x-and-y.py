class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        res = 0
        row, col = len(grid), len(grid[0])
        dp = [[(0,0) for _ in range(col+1)] for _ in range(row+1)]

        for i in range(1, row+1):
            for j in range(1, col+1):
                for_x, for_y = dp[i][j-1]
                prev_x, prev_y = dp[i-1][j]
                diag_x, diag_y = dp[i-1][j-1]

                curr_x = 1 if grid[i-1][j-1] == "X" else 0
                curr_y = 1 if grid[i-1][j-1] == "Y" else 0

                curr_x+=(for_x+prev_x-diag_x)
                curr_y+=(for_y+prev_y-diag_y)

                if curr_x>0 and curr_x == curr_y:
                    res+=1
                dp[i][j] = (curr_x, curr_y)
        return res

        