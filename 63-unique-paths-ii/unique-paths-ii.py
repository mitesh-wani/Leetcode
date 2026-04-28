class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
    # memorization time:O(m*n+m+n) space:O(m*n+m)
        # dp=[[-1]*n for _ in range(m)]
        # def uniquePathsCount(i,j):
        #     if i<0 or j<0:return 0
        #     if obstacleGrid[i][j]==1:return 0
        #     if i == 0 and j == 0:return 1
        #     if dp[i][j]!=-1:return dp[i][j]
        #     x=uniquePathsCount(i-1,j)
        #     y=uniquePathsCount(i,j-1)
        #     dp[i][j]=x+y
        #     return dp[i][j]
        # return uniquePathsCount(m-1,n-1)
    # tabulation:bottom to top in binary tree time:O(m*n) space:O(m*n)
        # dp=[[0]*n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if obstacleGrid[i][j]==1:
        #             dp[i][j] =0
        #         elif i == 0 and j == 0:
        #             dp[i][j]= 1
        #         else:
        #             right=dp[i][j-1] if j>0 else 0
        #             down=dp[i-1][j] if i>0 else 0
        #             dp[i][j]= right+down
        # return dp[m-1][n-1]
                    
    # space optimization in tabulation space:O(n)
        prior=[0]*n
        for i in range(m):
            curr=[0]*n
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    curr[j] =0 
                elif i == 0 and j == 0:
                    curr[j]= 1
                else:
                    down=prior[j] if i>0 else 0
                    right=curr[j-1] if j>0 else 0
                    curr[j]= right+down
            prior=curr
        return prior[n-1]