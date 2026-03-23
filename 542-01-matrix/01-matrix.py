from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])

        INF = float('inf')
        dist = [[INF]*col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    dist[i][j] = 0

        for i in range(row):
            for j in range(col):
                if mat[i][j] != 0:
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if i < row-1:
                    dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                if j < col-1:
                    dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)

        return dist