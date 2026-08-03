class disjoinSet:
    def __init__(self,n):
        self.parent=[-1]*n
    def find(self,node):
        if self.parent[node]<0:
            return node 
        self.parent[node]=self.find(self.parent[node])
        return self.parent[node]
    def union(self,a,b):
        parent_a=self.find(a)
        parent_b=self.find(b)
        if parent_b!=parent_a:
            if self.parent[parent_a]<self.parent[parent_b]:
                self.parent[parent_a]+=self.parent[parent_b]
                self.parent[parent_b]=parent_a
            else:
                self.parent[parent_b]+=self.parent[parent_a]
                self.parent[parent_a]=parent_b
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=0
        for i,j in edges:
            n=max(n,i,j)
        print(n)
        dis_set=disjoinSet(n)
        ans_edge=[-1,-1]
        for a,b in edges:
            if dis_set.find(a-1)!=dis_set.find(b-1):
                dis_set.union(a-1,b-1)
            else:
                ans_edge=[a,b]
        return ans_edge


        