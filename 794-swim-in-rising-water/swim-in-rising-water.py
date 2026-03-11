class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        n = len(grid)
        l, r = 0, max(max(row) for row in grid)
        visited = set()
        def dfs(coor, num):
            x, y = coor
            if grid[x][y]>num:
                return False

            for xx, yy in direction:
                dx, dy = x+xx, y+yy
                if dx<0 or dy<0 or dx>=n or dy>=n or (dx, dy) in visited:
                    continue
                if grid[dx][dy]>num:
                    continue
                if dx == dy == n-1:
                    return True
                visited.add((dx, dy))
                if dfs((dx, dy), num):
                    return True
            return False
        
        while l<r:
            m = (l+r)//2
            if dfs((0,0),m):
                r = m
            else:
                l = m+1
            visited.clear()
        return l
                

        