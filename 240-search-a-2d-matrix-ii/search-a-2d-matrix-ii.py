class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        visited = {}
        def getTarget(i, j):
            if i>=row or j>=col:
                return False
            if (i, j) in visited:
                return visited[(i,j)]
            if i<row and j<col and matrix[i][j] == target:
                return True
            visited[(i, j)] = getTarget(i+1, j) or getTarget(i, j+1)
            return visited[(i, j)]
        
        return getTarget(0,0)
        