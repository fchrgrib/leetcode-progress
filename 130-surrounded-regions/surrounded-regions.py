class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        r, c = len(board), len(board[0])
        q = []
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        for i in range(r):
            for j in (0, c - 1):
                if board[i][j] == "O":
                    q.append((i, j))

        for j in range(c):
            for i in (0, r - 1):
                if board[i][j] == "O":
                    q.append((i, j))

        idx = 0
        while idx < len(q):
            x, y = q[idx]
            idx += 1
            if board[x][y] != "O":
                continue

            board[x][y] = "#"
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == "O":
                    q.append((nx, ny))

        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
