class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        heap = []

        for val in counter.values():
            heapq.heappush(heap, val)
        
        while heap and heap[0]<=k:
            k-=heapq.heappop(heap)
        return len(heap)