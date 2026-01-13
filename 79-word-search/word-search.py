class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        queue = deque()
        r, c, lw = len(board), len(board[0]), len(word)
        visited = set()
        direct = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(coor, idx):
            nonlocal word, board, direct, visited, lw
            x, y = coor
            tmp = False
            for i, j in direct:
                dx, dy = x+i, y+j
                vis = (dx, dy)

                if dx<0 or dy<0 or dy>=c or dx>=r or vis in visited:
                    continue
                if board[dx][dy] == word[idx+1]:
                    if idx+1 == lw-1:
                        return True
                    visited.add(vis)
                    tmp|=dfs(vis, idx+1)
                    visited.remove(vis)
            return tmp



        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if lw == 1:
                        return True
                    vis = (i,j)
                    visited.add(vis)
                    if dfs(vis, 0):
                        return True
                    visited.remove(vis)
                    # queue.append([(i,j), 0])
                    # while queue:
                    #     tmp = queue.popleft()
                    #     if tmp[0] in visited:
                    #         continue
                    #     visited.add(tmp[0])

                    #     for k in direct:
                    #         dx = tmp[0][0] + k[0]
                    #         dy = tmp[0][1] + k[1]

                    #         if dx<0 or dy<0 or dy>=c or dx>=r:
                    #             continue
                            
                    #         if board[dx][dy] == word[tmp[1]+1] and (dx, dy) not in visited:
                    #             if tmp[1]+1 == lw-1:
                    #                 return True
                    #             queue.append([(dx, dy), tmp[1]+1])
                    # visited.clear()


        return False
        