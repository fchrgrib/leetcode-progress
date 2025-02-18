class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        memo = [[False for _ in range(n)] for _ in range(n)]
        global res
        res = []

        def bc(memo, row, step, n):
            global res
            if row == n:
                res.append(step[:])
                return
            tmp = ["." for i in range(n)]
            memo_tmp = memo.copy()
            
            

            for i in range(n):
                if memo_tmp[row][i]:
                    continue
                memo_tmp[row][i] = True
                tmp[i] = "Q"
                step.append("".join(tmp))
                tmp[i] = "."
                for j in range(1, n):
                    if row+j>=n:
                        break
                    memo_tmp[row+j] = memo[row+j][:]
                    if i-j>=0 and row+j<n:
                        memo_tmp[row+j][i-j] = True
                    if row+j<n:
                        memo_tmp[row+j][i] = True
                    if i+j<n and row+j<n:
                        memo_tmp[row+j][i+j] = True
                # print(row," ",memo_tmp)
                bc(memo_tmp[:], row+1, step, n)
                memo_tmp[row][i] = False
                memo_tmp = memo.copy()
                step.pop()
        bc(memo, 0, [], n)
        return res
        