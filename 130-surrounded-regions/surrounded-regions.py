class Solution:
    def dfs(self,i,j,board,visited):
        visited[i][j]=True
        direction=[(-1,0),(1,0),(0,-1),(0,1)]
        for dr,dc in direction:
            nr,nc=dr+i,dc+j
            if 0<=nr<len(board) and 0<=nc<len(board[0]) and not visited[nr][nc] and board[nr][nc] == 'O':
                self.dfs(nr,nc,board,visited)
        return 
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])

        visited=[[False for _ in range(n)] for _ in range(m)]

        for i in range(n):
            if board[0][i]=="O" and not visited[0][i]:
                self.dfs(0,i,board,visited)
            if board[m-1][i]=="O" and not visited[m-1][i]:
                self.dfs(m-1,i,board,visited)
        for i in range(m):
            if board[i][0]=="O" and not visited[i][0]:
                self.dfs(i,0,board,visited)
            if board[i][n-1]=="O" and not visited[i][n-1]:
                self.dfs(i,n-1,board,visited)
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and not visited[i][j]:
                    board[i][j]="X"


        