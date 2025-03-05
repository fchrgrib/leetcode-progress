class Solution:
    def coloredCells(self, n: int) -> int:
        sum = 0
        for i in range(1, n+1):
            sum+=(i*2-1)
        for i in range(n-1, 0, -1):
            sum+=(i*2-1)
        return sum
        