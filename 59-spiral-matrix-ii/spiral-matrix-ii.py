class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]

        def fill_res(start, col, row, sum) :
            if start >= col or start >= row:
                return
            
            for i in range(start, col):
                res[start][i] = sum
                sum+=1
            for i in range(start+1, row):
                res[i][col-1] = sum
                sum+=1
            
            if start<col-1:
                for i in range(col-2, start-1,-1):
                    res[row-1][i] = sum
                    sum+=1

            if start<row-1:
                for i in range(row-2, start,-1):
                    res[i][start] = sum
                    sum+=1

            fill_res(start +1, col-1, row-1, sum)

        fill_res(0, n, n, 1)
        return res