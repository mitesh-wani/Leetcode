from queue import PriorityQueue
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        adj=[[]for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                adj[i].append((dist,j))
                adj[j].append((dist, i))
        
        pq=PriorityQueue()
        pq.put((0,0,-1)) #dist,point,parent
        visited=[False]*n
        ans=0
        edges=[]
        while not pq.empty():
            d,curr_node,parent_node=pq.get()
            if visited[curr_node]:
                continue
            if not visited[curr_node]:
                ans+=d
                visited[curr_node]=True
                edges.append((parent_node,curr_node))
            for w,neigh in adj[curr_node]:
                if not visited[neigh]:
                    pq.put((w,neigh,curr_node))

        return ans