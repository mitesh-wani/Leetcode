class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distanceMatrix=[[float('inf')]*n for _ in range(n)]
        for i in range(n):
            distanceMatrix[i][i]=0 
        for u,v,w in edges:
            distanceMatrix[u][v]=w
            distanceMatrix[v][u]=w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distanceMatrix[i][j]>distanceMatrix[i][k]+distanceMatrix[k][j]:
                        distanceMatrix[i][j]=distanceMatrix[i][k]+distanceMatrix[k][j]
        ans=-1
        minCities=float('inf')

        for i in range(n-1,-1,-1):
            count=0
            for j in range(n):
                if distanceMatrix[i][j]<=distanceThreshold:
                    count+=1
            if count<minCities:
                minCities=count
                ans=i
        return ans