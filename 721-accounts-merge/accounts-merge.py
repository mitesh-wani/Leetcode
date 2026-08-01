class disjoinSet:
    def __init__(self,size):
        self.parent=[-1]*size
    def find(self,node):
        if self.parent[node]<0:
            return node
        self.parent[node]=self.find(self.parent[node])
        return  self.parent[node]
    def union(self,a,b):
        parent_a=self.find(a)
        parent_b=self.find(b)
        if parent_a!=parent_b:
            if self.parent[parent_a]<=self.parent[parent_b]:
                self.parent[parent_a]+=self.parent[parent_b]
                self.parent[parent_b]=parent_a
            else:
                self.parent[parent_b]+=self.parent[parent_a]
                self.parent[parent_a]=parent_b
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        dis_set=disjoinSet(n)
        m={}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                email=accounts[i][j]
                if email not in m:
                    m[email]=i
                else:
                    dis_set.union(i,m[email])
        ans=[[]for _ in range(n)]
        for i in range(n):
            ans[i].append(accounts[i][0])
        for email, idx in m.items():
            overallParent=dis_set.find(idx)
            ans[overallParent].append(email)
        print(ans)
        result=[]
        for i in range(n):
            if dis_set.parent[i]<0:
                ans[i][1:]=sorted(ans[i][1:])
                result.append(ans[i])

        return result
