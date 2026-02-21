class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area, curr_area = 0, 0
        direction = [(1,0), (0,1), (0,-1), (-1,0)]
        row, col = len(grid), len(grid[0])
        queue = deque()

        if row == col == 1:
            return grid[0][0]
        

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    curr_area = 1
                    grid[i][j] = 0
                    queue.append((i,j))

                    while queue:
                        x, y = queue.popleft()

                        for xx, yy in direction:
                            dx, dy = x+xx, y+yy

                            if dx<0 or dy<0 or dx>=row or dy>=col:
                                continue
                            
                            if grid[dx][dy] == 0:
                                continue
                            
                            curr_area+=1
                            grid[dx][dy] = 0
                            queue.append((dx,dy))
                    max_area = max(max_area, curr_area)
        return max_area