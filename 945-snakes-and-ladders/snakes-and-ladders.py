class Solution:
    def snakesAndLadders(self, b: List[List[int]]) -> int:
        n = len(b)
        visited = set()
        q = deque()
        q.append((1, 0))
        
        while q:
            cell, moves = q.popleft()
            if cell == n * n:
                return moves
            if cell in visited:
                continue
            visited.add(cell)
            
            for i in range(1, 7):
                next_cell = cell + i
                if next_cell > n * n:
                    break

                row = n - 1 - (next_cell - 1) // n
                col = (next_cell - 1) % n
                if (n - 1 - row) % 2 == 1:
                    col = n - 1 - col
                
                if b[row][col] != -1:
                    next_cell = b[row][col]
                
                if next_cell not in visited:
                    q.append((next_cell, moves + 1))
        return -1
        