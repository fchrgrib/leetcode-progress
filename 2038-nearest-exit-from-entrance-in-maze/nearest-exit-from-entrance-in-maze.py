class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        start_r, start_c = entrance
        
        queue = deque([(start_r, start_c, 0)])
        maze[start_r][start_c] = '+'
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c, dist = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == ".":
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return dist + 1
                    
                    maze[nr][nc] = '+'
                    queue.append((nr, nc, dist + 1))
        
        return -1


        