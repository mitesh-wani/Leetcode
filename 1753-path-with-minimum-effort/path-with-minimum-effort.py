from queue import PriorityQueue
class Solution:
    

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m=len(heights)
        n=len(heights[0])
        start=(0,0)
        end=(m-1,n-1)
        dist=[[float('inf')]*n for _ in range(m)]
        dist[0][0]=0 
        pq=PriorityQueue()
        pq.put((0,(0,0)))#dist,row,col
        ans=0
        while not pq.empty():
            curr_dist,pos=pq.get()
            r,c=pos
            if curr_dist >dist[r][c]:
                continue
            
            if pos==end:
                return curr_dist
            directions=[(1,0),(-1,0),(0,-1),(0,1)]
            for dr,dc in directions:
                nr,nc=dr+r,dc+c
                if nr>=0 and nr<m and nc>=0 and nc<n:
                    new_dist=max(curr_dist,abs(heights[nr][nc]-heights[r][c]))
                    if new_dist<dist[nr][nc]:
                        dist[nr][nc]=new_dist
                        pq.put((dist[nr][nc],(nr,nc)))


        