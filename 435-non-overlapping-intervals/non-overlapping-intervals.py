class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        heap = []
        res = 0

        for i in intervals:
            heapq.heappush(heap, (i[0], i[1]))
        
        # print(SortedList(heap))
        x, y = heapq.heappop(heap)

        while heap:
            tmp_x, tmp_y = heapq.heappop(heap)

            if tmp_x<y:
                # print(f"ini tmp: ({tmp_x}, {tmp_y})")
                # print(f"ini ril: ({x}, {y})")
                if y>tmp_y:
                    x, y = tmp_x, tmp_y
                res+=1
            else:
                y = tmp_y
                x = tmp_x
        return res