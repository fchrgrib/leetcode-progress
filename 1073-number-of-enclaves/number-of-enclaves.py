class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        queue = deque()
        row, col = len(grid), len(grid[0])
        direction = [(0,1), (1,0), (-1,0), (0,-1)]
        count = 0

        step_col, step_row = [0, col-1], [0, row-1]

        def bfs(i, j):
            queue.append((i, j))

            while queue:
                x, y = queue.popleft()
                
                for xx, yy in direction:
                    dx = x+xx
                    dy = y+yy

                    if dx<0 or dy<0 or dx>=row or dy>=col:
                        continue
                    if grid[dx][dy] != 1:
                        continue
                    grid[dx][dy] = 2
                    queue.append((dx, dy))


        for cl in step_col:
            for i in range(row):
                if grid[i][cl] != 1:
                    continue
                grid[i][cl] = 2
                bfs(i, cl)
        for rw in step_row:
            for i in range(col):
                if grid[rw][i] != 1:
                    continue
                grid[rw][i] = 2
                bfs(rw, i)
        print(grid)
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 1:
                    continue
                count+=1
        return count
        
                
                


        