class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = {}

        for i in words:
            if i not in mp:
                mp[i] = 0
            mp[i]+=1
        res = []

        for ky, v in mp.items():
            heapq.heappush(res, (-v, ky))
        res.sort()
        return [res[i][1] for i in range(k)]
        