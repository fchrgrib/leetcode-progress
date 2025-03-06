class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = (0, 0)
        r = (len(matrix)-1, len(matrix[0])-1)
        if matrix[l[0]][l[1]] == target or matrix[r[0]][r[1]] == target:
            return True
        temp = (len(matrix[0])*l[0]+l[1] + len(matrix[0])*r[0]+r[1])//2
        m = (temp//len(matrix[0]), temp%len(matrix[0]))

        while len(matrix[0])*l[0]+l[1] < len(matrix[0])*r[0]+r[1]:
            if matrix[m[0]][m[1]] == target:
                return True
            if matrix[l[0]][l[1]] == target or matrix[r[0]][r[1]] == target:
                return True
            if matrix[m[0]][m[1]] > target:
                if m[1]-1<0:
                    x = m[0]-1
                    y = len(matrix[0])-1
                else:
                    x = m[0]
                    y = m[1]-1
                r = (x, y)
            if matrix[m[0]][m[1]] < target:
                if m[1]+1>len(matrix[0])-1:
                    x = m[0]+1
                    y = 0
                else:
                    x = m[0]
                    y = m[1]+1
                l = (x, y)
            temp = (len(matrix[0])*l[0]+l[1] + len(matrix[0])*r[0]+r[1])//2
            m = (temp//len(matrix[0]), temp%len(matrix[0]))

        return False

