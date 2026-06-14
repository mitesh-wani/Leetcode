from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=[[False for _ in range(n)]for _  in range(m)]
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append(((i,j),0))
                    visited[i][j] = True
        ans_t=0
        while q:
            (r,c),t=q.popleft()
            direction=[(-1,0),(1,0),(0,-1),(0,1)]
            for dr,dc in direction:
                nr,nc=dr+r,dc+c
                if 0<=nr<m and 0<=nc<n and not visited[nr][nc] and grid[nr][nc]==1:
                    ans_t=max(ans_t,t+1)
                    visited[nr][nc]=True
                    q.append(((nr,nc),t+1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not visited[i][j]:
                    return -1
        return ans_t
