class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row+1)]

        for i in range(1,row+1):
            for j in range(col):
                if j == 0 and j == col-1:
                    dp[i][j] = matrix[i-1][j] + dp[i-1][j]
                elif j == 0:
                    dp[i][j] = min(matrix[i-1][j] + dp[i-1][j], matrix[i-1][j] + dp[i-1][j+1])
                elif j == col-1:
                    dp[i][j] = min(matrix[i-1][j] + dp[i-1][j], matrix[i-1][j] + dp[i-1][j-1])
                else:
                    dp[i][j] = min(matrix[i-1][j] + dp[i-1][j], matrix[i-1][j] + dp[i-1][j+1], matrix[i-1][j] + dp[i-1][j-1])
                

        return min(dp[row])
        