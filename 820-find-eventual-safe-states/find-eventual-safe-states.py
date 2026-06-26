class Solution:
    def dfs(self,start,adj,visited,path,result):
        visited[start]=True
        path[start]=True
        
        for k in adj[start]:
            if not visited[k]:
                if self.dfs(k,adj,visited,path,result):
                    return True
            elif path[k]:
                return True
        path[start]=False
        result.append(start)
        return False
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        visited=[False]*n 
        path=[False]*n 
        result=[]
        for i in range(n):
            if not visited[i]:
                self.dfs(i,graph,visited,path,result)
        result.sort()     
        return result