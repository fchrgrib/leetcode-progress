class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        res = [[0 for _ in range(col)] for _ in range(row)]

        if obstacleGrid[row-1][col-1] == 1:
            return 0
        if row == 1 and col == 1 and obstacleGrid[row-1][col-1] == 0:
            return 1
        res[row-1][col-1] = 1
        for i in range(row-2, -1, -1):
            if obstacleGrid[i][col-1] == 1:
                continue
            res[i][col-1] = res[i+1][col-1]

        for i in range(col-2, -1, -1):
            if obstacleGrid[row-1][i] == 1:
                continue
            res[row-1][i] = res[row-1][i+1]

        res[0][0] = 0

        if row == 1 and col>1:
            for j in range(col-2,-1, -1):
                if obstacleGrid[0][j] == 1:
                    continue
                res[0][j] = res[i][j+1]
        elif row>1 and col == 1:
            for j in range(row-2,-1, -1):
                if obstacleGrid[j][0] == 1:
                    continue
                res[j][0] = res[j+1][0]
        else:
            for i in range(row-2, -1, -1):
                for j in range(col-2,-1, -1):
                    if obstacleGrid[i][j] == 1:
                        continue
                    res[i][j] = res[i+1][j] + res[i][j+1]
                    print(res[i+1][j] + res[i][j+1])

        return res[0][0]
        