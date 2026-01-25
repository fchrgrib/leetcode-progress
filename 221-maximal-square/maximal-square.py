class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = {}
        max_square = 0
        r = len(matrix)
        c = len(matrix[0])

        def get_max(direct: str, i: int, j: int):
            nonlocal dp, matrix, r, c
            if i<r and j<c and matrix[i][j] == "0":
                return -1 
            store = (direct, i, j)
            if store in dp:
                    return dp[store]
            if direct == "r" and i>=r-1:
                return i
            if direct == "c" and j>= c-1:
                return j
            
            if direct == "r":
                dp[store] = store[1]
            else:
                dp[store] = store[2]

            if direct == "r":
                if i+1<r and j<c and matrix[i+1][j] == "1":
                    dp[store] = get_max(direct, i+1, j)
                return dp[store]
            else:
                if j+1<c and i<r and matrix[i][j+1] == "1":
                    dp[store] = get_max(direct, i, j+1)
                return dp[store]
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == "1":
                    sq = 0
                    mr, mc = get_max("r", i, j+sq), get_max("c", i+sq, j)
                    if max_square> (mr-i)**2 or max_square>(mc-j)**2:
                        continue
                    while sq<=mr-i and sq<=mc-j:
                        sq+=1
                        mr, mc = get_max("r", i, j+sq), get_max("c", i+sq, j)
                    # print(dp)
                    max_square = max(max_square, sq**2)
        return max_square


        