class DisjointSet:
    def __init__(self, size):
        self.parent = [-1] * size

    def find(self, node):
        if self.parent[node] < 0:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def unionSize(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            if self.parent[parent_a] < self.parent[parent_b]:
                temp = self.parent[parent_b]
                self.parent[parent_b] = parent_a
                self.parent[parent_a] += temp
            else:
                temp = self.parent[parent_a]
                self.parent[parent_a] = parent_b
                self.parent[parent_b] += temp

class Solution:
    import math
    def largestComponentSize(self, nums: List[int]) -> int:
        n=len(nums)
        #dis_set=DisjointSet(n)
# this logic is correct but time complexity n^2 
        # for i in range(n):
        #     for j in range(i+1,n):
        #         f=math.gcd(nums[i],nums[j])
        #         if f>1:
        #             dis_set.unionSize(i,j)
        # ans=1
        # for i in dis_set.parent:
        #     ans=max(-i,ans)
        
        # return ans

# time:O(n*sprt(m))   
        max_val=max(nums)
        dis_set=DisjointSet(max_val+1)
        for i in range(n):
            temp=nums[i]
            d=2
            while d*d<=temp:
                if temp%d==0:
                    dis_set.unionSize(nums[i],d)
                    while temp%d==0:
                        temp//=d
                d+=1
            if temp>1:
                dis_set.unionSize(nums[i],temp)

        counts={}
        ans=0        
                
        for num in nums:
            root=dis_set.find(num)
            counts[root]=counts.get(root,0)+1
            ans=max(ans,counts[root])
        return ans