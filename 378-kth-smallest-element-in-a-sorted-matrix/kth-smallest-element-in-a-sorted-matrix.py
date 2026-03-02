class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap_mx, heap_min = [], []
        ln = len(matrix)*len(matrix)

        for m_x in matrix:
            for i in m_x:
                if heap_mx and -heap_mx[0]>i:
                    heapq.heappush(heap_mx, -i)
                else:
                    heapq.heappush(heap_min, i)
                

                if heap_min and ln-k<len(heap_min):
                    heapq.heappush(heap_mx,-heapq.heappop(heap_min))
                elif heap_mx and len(heap_mx)>k:
                    heapq.heappush(heap_min,-heapq.heappop(heap_mx))
        return -heap_mx[0]
        