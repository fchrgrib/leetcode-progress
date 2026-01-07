class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = deque()
        r = len(board)
        c = len(board[0])
        direct = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        for i in range(c):
            if board[0][i] == "O":
                queue.append((0, i))
        for i in range(r):
            if board[i][0] == "O":
                queue.append((i, 0))
        for i in range(c-1, -1, -1):
            if board[r-1][i] == "O":
                queue.append((r-1, i))
        for i in range(r-1, -1, -1):
            if board[i][c-1] == "O":
                queue.append((i, c-1))
        while queue:
            tmp = queue.popleft()
            if tmp in visited:
                continue
            visited.add(tmp)

            for x, y in direct:
                ix = tmp[0]+x
                iy = tmp[1]+y
                if ix<0 or ix>=r or iy<0 or iy>=c:
                    continue
                if board[ix][iy] == "O":
                    queue.append((ix, iy))



        for i in range(r):
            for j in range(c):
                if board[i][j] == "O" and (i, j) not in visited:
                    queue.append((i,j))

                    while queue:
                        tmp = queue.popleft()
                        board[tmp[0]][tmp[1]] = "X"

                        for x, y in direct:
                            ix = tmp[0]+x
                            iy = tmp[1]+y
                            if ix<0 or ix>=r or iy<0 or iy>=c:
                                continue
                            if board[ix][iy] == "O":
                                board[ix][iy] = "X"
                                queue.append((ix, iy))

        