class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        par, rank = {}, {}

        def find_par(s):
            nonlocal par
            if s not in par:
                par[s] = s
            
            tmp = par[s]
            while tmp!=par[tmp]:
                tmp = find_par(tmp)
            return tmp
        
        def union_find(a, b):
            nonlocal rank, par
            p1, p2 = find_par(a), find_par(b)

            if p1 == p2:
                return True
            
            if p1 not in rank:
                rank[p1] = 1
            if p2 not in rank:
                rank[p2] = 1
            
            r1, r2 = rank[p1], rank[p2]

            if r1>r2:
                rank[p1]+=1
                par[p2] = p1
            else:
                rank[p2]+=1
                par[p1] = p2
            return False
        
        fls = []
        for i in equations:
            if i[1]+i[2] == "!=":
                fls.append(i)
                continue
            if i[1]+i[2] == "==":
                union_find(i[0], i[3])
        for i in fls:
            if find_par(i[0]) == find_par(i[3]):
                return False
        return True
