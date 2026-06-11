class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        visited=[[False for _ in range(n)] for _ in range(m)]
        startColor=image[sr][sc]
        
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or visited[i][j] or image[i][j]!=startColor:
                return
            visited[i][j]=True
            image[i][j]=color
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        dfs(sr,sc)

        return image


        