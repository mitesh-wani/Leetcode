from queue import PriorityQueue
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
# not solved using dijkstra algorithm
        # dist=[float('inf')]*n 
        # pq=PriorityQueue()
        # dist[0]=0
        # pq.put((0,0)) #dist,node
        # print(roads[1][0]==2)
        # while not pq.empty():
        #     curr_dist,curr_node=pq.get()
        #     if curr_dist>dist[curr_node]:
        #         continue
        #     for u,v,wt in roads:
        #         if u==curr_node:
        #             new_dist=curr_dist+wt
        #             if new_dist<dist[v]:
        #                 dist[v]=new_dist
        #                 pq.put((new_dist,v))
        # print(dist)
            
        adj=[[] for _ in range(n)]
        for u,v,wt in roads:
            adj[u-1].append((v-1,wt))
            adj[v-1].append((u-1,wt))
        ans=float('inf')
        visited=[False]*n 
        def dfs(i,visited):
            nonlocal ans
            visited[i]=True
            for nei,wt in adj[i]:
                ans=min(ans,wt)
                if not visited[nei]:
                    dfs(nei,visited)
        dfs(0,visited)
        return ans