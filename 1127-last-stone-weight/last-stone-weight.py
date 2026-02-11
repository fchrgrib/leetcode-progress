class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for i in stones:
            heapq.heappush(heap, -i)

        while heap:
            tmp_1 = heapq.heappop(heap)
            if not heap:
                return -tmp_1
            tmp_2 = heapq.heappop(heap)

            if tmp_1 == tmp_2:
                continue
            
            heapq.heappush(heap, -abs(tmp_1-tmp_2))
        return 0

        