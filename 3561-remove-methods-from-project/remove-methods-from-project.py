class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj=[[]for _ in range(n)]
        for i ,j in invocations:
            adj[i].append(j)
        #print(adj)
        visited=[False]*n
        q=collections.deque([k])
        visited[k]=True
        while q:
            u=q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        #print(visited)
        remove=False
        for i , j in invocations:
            if not visited[i] and visited[j]:
                remove=True
                break
        if remove:
            return list(range(n))
        return [i for i in range(n) if not visited[i]]