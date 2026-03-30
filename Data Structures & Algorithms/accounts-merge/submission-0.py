class UnionFind: 
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n 
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y): 
        px, py = self.find(x), self.find(y)
        if px == py: 
            return False 
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        self.components -= 1
        return True 
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # accounts[i][0] = name; rest are emails for that account 
        # two accounts belong to same person if there is some common email to both accounts 
        # two people can have same name 
        # a person can have any number of accounts; a person can have only one name
        # merge accounts: if there is some common email to both accounts 
        # return: [account name, ...emails in sorted order]
        uf = UnionFind(len(accounts))
        email_to_accounts = collections.defaultdict(int)

        for i, emails in enumerate(accounts): 
            for email in emails[1:]:
                if email in email_to_accounts:
                    uf.union(i, email_to_accounts[email])
                else:
                    email_to_accounts[email] = i
        
        email_group = defaultdict(list)
        for email, acc_idx in email_to_accounts.items():
            leader_acc = uf.find(acc_idx)
            email_group[leader_acc].append(email)
        print(email_group)
        res = []
        for acc_idx, emails in email_group.items():
            print(emails)
            res.append([accounts[acc_idx][0]] + sorted(emails))
        return res





        