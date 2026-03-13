class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        row, col = len(grid), len(grid[0])
        visited = [[0]*col for _ in range(row)]
        direction = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(x, y, px, py):
            visited[x][y] = 1

            for dx, dy in direction:
                nx, ny = x+dx, y+dy

                if nx<0 or ny<0 or nx>=row or ny>=col:
                    continue
                if grid[nx][ny] != grid[x][y]:
                    continue

                if nx == px and ny == py:
                    continue

                if visited[nx][ny]:
                    return True

                if dfs(nx, ny, x, y):
                    return True

            return False

        for i in range(row):
            for j in range(col):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1):
                        return True

        return False