class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r, c = len(heights), len(heights[0])
        wg = [[float("inf") for _ in range(c)] for _ in range(r)]
        direct = [(0,1), (1,0), (-1,0), (0,-1)]

        wg[0][0] = 0

        heap = []
        heapq.heappush(heap, (0,(0,0)))

        while heap:
            effort, coor = heapq.heappop(heap)
            x, y = coor
            curr = heights[x][y]

            for i in direct:
                dx, dy = x + i[0], y + i[1]

                if dx<0 or dy<0 or dx>=r or dy>=c:
                    continue
                
                num = heights[dx][dy]
                tmp_max = max(effort, abs(curr-num))
                if tmp_max<wg[dx][dy]:
                    wg[dx][dy] = tmp_max
                    heapq.heappush(heap, (tmp_max, (dx, dy)))

        return wg[r-1][c-1]
        