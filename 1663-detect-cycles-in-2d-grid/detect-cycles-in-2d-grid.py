class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        row, col = len(grid), len(grid[0])
        rank = [[1 for _ in range(col)] for _ in range(row)]
        parent = {(i, j):(i, j) for j in range(col) for i in range(row)}
        direction = [(-1, 0), (0,-1)]
        
        def get_parent(coor):
            tmp = parent[coor]
            while tmp != parent[tmp]:
                tmp = parent[tmp]
            return tmp
        
        def union_find(coor1, coor2):
            p1, p2 = get_parent(coor1), get_parent(coor2)

            x1, y1 = p1
            x2, y2 = p2

            if rank[x1][y1] >= rank[x2][y2]:
                rank[x1][y1]+=rank[x2][y2]
                parent[p2] = p1
            else:
                rank[x2][y2]+=rank[x1][y1]
                parent[p1] = p2
        par = (-1, -1)
        prev_parent = (-1, -1)
        for i in range(row):
            for j in range(col):
                for x, y in direction:
                    dx, dy = i+x, j+y
                    if dx<0 or dy<0 or dx>=row or dy>=col:
                        continue
                    if grid[dx][dy] != grid[i][j]:
                        continue
                    par = get_parent((dx, dy))
                    if par == prev_parent:
                        return True
                    prev_parent = par
                    union_find((dx, dy), (i, j))
                par = (-1, -1)
                prev_parent = (-1, -1)
        return False
        

        