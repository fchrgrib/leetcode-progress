class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        res = []
        temp = {}
        for i in range(1,n*n+1):
            temp[i] = True
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in temp:
                    res.append(grid[i][j])
                    continue
                del temp[grid[i][j]]

        for k, _ in temp.items():
            res.append(k)
        return res
        