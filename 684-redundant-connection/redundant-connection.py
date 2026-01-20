class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = {j: 1 for i in edges for j in i}
        par = {j:j for i in edges for j in i}

        def find_par(n):
            nonlocal par
            tmp = par[n]
            while tmp!=par[tmp]:
                tmp = par[tmp]
            return tmp
        
        def is_same_par(n1, n2):
            nonlocal rank, par
            p1, p2 = find_par(n1), find_par(n2)
            if p1 == p2:
                return True
            
            rank1, rank2 = rank[p1], rank[p2]

            if rank1>rank2:
                rank[p1]+=1
                par[p2] = p1
            else:
                rank[p2]+=1
                par[p1] = p2
            return False
        
        for i in edges:
            if is_same_par(i[0], i[1]):
                return i
        return edges[0]
        

        