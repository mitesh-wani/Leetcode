class Solution:
    def dfs(self,curr,parent,adj,visited,timer,disc,low,bridges):
        visited[curr]=True
        disc[curr]=low[curr]=timer[0]
        timer[0]+=1
        for k in adj[curr]:
            if k!=parent:
                if not visited[k]:
                    self.dfs(k,curr,adj,visited,timer,disc,low,bridges)
                    low[curr]=min(low[k],low[curr])
                    if low[k]>disc[curr]:
                        bridges.append([k,curr])
                else:
                    low[curr]=min(disc[k],low[curr])
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        visited=[False]*n
        timer=[1]
        disc=[0]*n
        low=[0]*n
        bridges=[]
        adj=[[]for _ in range(n)]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        for i in range(n):
            if not visited[i]:
                self.dfs(i,-1,adj,visited,timer,disc,low,bridges)
        return bridges