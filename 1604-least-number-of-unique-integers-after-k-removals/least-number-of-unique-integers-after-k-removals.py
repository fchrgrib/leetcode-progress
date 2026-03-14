class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        heap = list(counter.values())
        heapq.heapify(heap)
        
        while heap and heap[0]<=k:
            k-=heapq.heappop(heap)
        return len(heap)