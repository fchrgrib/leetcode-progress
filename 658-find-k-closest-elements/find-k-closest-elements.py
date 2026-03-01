class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap_k, heap_nk = [], []
        res = []


        for num in arr:
            diff = abs(num-x)
            if heap_k and -heap_k[0][0]>diff:
                heapq.heappush(heap_k, (-diff, num))
            else:
                heapq.heappush(heap_nk, (diff, num))
            
            if heap_k and len(heap_k)>k:
                df, nm = heapq.heappop(heap_k)
                heapq.heappush(heap_nk, (-df, nm))
            elif heap_nk and len(arr) - k < len(heap_nk):
                df, nm = heapq.heappop(heap_nk)
                heapq.heappush(heap_k, (-df, nm))
        while heap_k:
            res.append(heapq.heappop(heap_k)[1])
        return sorted(res)
        