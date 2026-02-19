class Solution:
    def reorganizeString(self, s: str) -> str:
        ls = len(s)

        if ls == 1:
            return s

        prev = (-1, -1)
        heap = []
        res = ""
        ct = Counter(s)

        for key, val in ct.items():
            heapq.heappush(heap, (-val, key))
        
        while heap:
            count, chr = heapq.heappop(heap)

            if -count > (ls//2 + ls%2):
                return ""
            res+=chr
            if prev != (-1, -1) and prev[0] != 0:
                heapq.heappush(heap, prev)
            if count<0:
                prev = (count+1, chr)
        return res
        