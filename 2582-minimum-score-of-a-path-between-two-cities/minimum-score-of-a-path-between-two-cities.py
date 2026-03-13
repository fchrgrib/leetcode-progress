class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rank = {i:1 for i in range(1,n+1)}
        parent = {i:i for i in range(1, n+1)}
        min_dist = {i:float("inf") for i in range(1, n+1)}


        def get_parent(i):
            par = parent[i]
            while par != parent[par]:
                par = parent[par]
            return par
        
        def union_find(node1, node2):
            par1, par2 = get_parent(node1), get_parent(node2)

            if par1 == par2:
                return
            
            if rank[par1]>rank[par2]:
                rank[par1]+=rank[par2]
                parent[par2] = par1
            else:
                rank[par2]+=rank[par1]
                parent[par1] = par2
        for fr, to, dist in roads:
            union_find(fr, to)

        for fr, to, dist in roads:
            par = get_parent(fr)
            min_dist[par] = min(min_dist[par], dist)
        return min_dist[get_parent(1)]

        