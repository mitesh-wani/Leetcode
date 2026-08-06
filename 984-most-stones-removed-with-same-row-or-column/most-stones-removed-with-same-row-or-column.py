class disjointSet:
    def __init__(self, size):
        self.parent = [-1] * size

    def find(self, node):
        if self.parent[node] < 0:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            if self.parent[parent_a] < self.parent[parent_b]:
                self.parent[parent_a] += self.parent[parent_b]
                self.parent[parent_b] = parent_a
            else:
                self.parent[parent_b] += self.parent[parent_a]
                self.parent[parent_a] = parent_b

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        dis_set=disjointSet(n)
        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    dis_set.union(i,j)
        count=0
        for i in range(n):
            if dis_set.parent[i]<0:
                count+=1
        return n-count

        