class Solution:
    def dfs(self,i,j,board,visited,word,idx):
        if idx==len(word):
            return True
        m=len(board)
        n=len(board[0])
        if m<=i or i<0 or n<=j or j<0 or visited[i][j] or word[idx]!=board[i][j]:
            return False
        visited[i][j]=True
        direction=[(-1,0),(1,0),(0,-1),(0,1)]
        for dr,dc in direction:
            nr,nc=dr+i,dc+j
            #if 0<=nr<m and 0<=nc<n and not visited[nr][nc] and word[idx]==board[nr][nc]:
            if self.dfs(nr,nc,board,visited,word,idx+1):
                visited[i][j]=False
                return True
        visited[i][j]=False
        return False



    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        visited=[[False for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if word[0]==board[i][j]:
                    if self.dfs(i,j,board,visited,word,0):
                        return True
        return False
        