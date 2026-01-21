class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = UnionFind(len(accounts))
        email_to_acc_id = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_acc_id:
                    dsu.union(i, email_to_acc_id[email])
                else:
                    email_to_acc_id[email] = i
        
        merged_emails = defaultdict(list)
        
        for email, owner_id in email_to_acc_id.items():
            root_id = dsu.find(owner_id)
            merged_emails[root_id].append(email)
        
        res = []
        for root_id, emails in merged_emails.items():
            name = accounts[root_id][0]
            res.append([name] + sorted(emails))
            
        return res