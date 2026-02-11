class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        direct = [(1,1), (-1,-1), (1,0), (0,1), (-1,0),(0,-1), (-1,1), (1,-1)]

        row, col = len(board), len(board[0])

        for i in range(row):
            for j in range(col):
                live_count = 0

                for x, y in direct:
                    dx, dy = i+x, j+y
                    if dx<0 or dy<0 or dx>=row or dy>=col:
                        continue
                    if board[dx][dy] == 1 or board[dx][dy] == 3:
                        live_count+=1
                if board[i][j] == 1 and (live_count<2 or live_count>3):
                    board[i][j] = 3
                elif board[i][j] == 0 and live_count == 3:
                    board[i][j] = 2
        for i in range(row):
            for j in range(col):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1

        