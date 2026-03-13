class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = list(range(n+1))
        rank = [1]*(n+1)
        min_dist = [float("inf")]*(n+1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a,b,d in roads:
            pa, pb = find(a), find(b)

            if pa != pb:
                if rank[pa] < rank[pb]:
                    pa, pb = pb, pa
                parent[pb] = pa
                rank[pa] += rank[pb]
                min_dist[pa] = min(min_dist[pa], min_dist[pb], d)
            else:
                min_dist[pa] = min(min_dist[pa], d)

        return min_dist[find(1)]