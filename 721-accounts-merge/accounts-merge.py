class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        par = {}
        la = len(accounts)
        par_node = {i:i for i in range(la)}
        res = {}

        def change_all_par(l_a, val):
            nonlocal par
            for i in l_a:
                par[i] = val

        for _ in range(la):
            for i in range(la):
                tmp_node = i
                for j in range(1, len(accounts[i])):
                    tmp_e = accounts[i][j]
                    if tmp_e not in par:
                        par[tmp_e] = i
                    else:
                        tmp_node = min(tmp_node, par[tmp_e])
                if tmp_node != i:
                    change_all_par(accounts[i][1:], tmp_node)
                par_node[i] = tmp_node

        for k, v in par_node.items():
            if (accounts[k][0], v) not in res:
                res[(accounts[k][0], v)] = set(accounts[k][1:])
                continue
            
            res[(accounts[k][0], v)].update(accounts[k][1:])

        
        return [[k[0]] + sorted(list(v)) for k, v in res.items()]



        
        
        

        