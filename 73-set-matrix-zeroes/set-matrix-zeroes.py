class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        i_z = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    i_z.append([i, j])

        for i in i_z:
            for j in range(len(matrix[0])):
                matrix[i[0]][j] = 0
            for j in range(len(matrix)):
                matrix[j][i[1]] = 0
        