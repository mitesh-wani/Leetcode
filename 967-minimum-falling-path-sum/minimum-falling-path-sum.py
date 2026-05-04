class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # recursion time:O(n*3^n) space:O(n^2)
        # def helper(i,j):
        #     if j>n-1 or j<0:return float('inf')
        #     if i==n-1:return matrix[n-1][j]
        #     down=helper(i+1,j)
        #     right_d=helper(i+1,j+1)
        #     left_d=helper(i+1,j-1)

        #     return matrix[i][j]+min(down,right_d,left_d)
        # minVal=float('inf')
        # for j in range(n):
        #     minVal=min(minVal,helper(0,j,dp))
        # return minVal

        # memorization time:O(3^n) space:O(n^2)
        # dp=[[-1]*n for _ in range(n)]
        # def helper(i,j,dp):
        #     if j>n-1 or j<0:return float('inf')
        #     if i==n-1:return matrix[n-1][j]
        #     if dp[i][j]!=-1:return dp[i][j]
        #     down=helper(i+1,j,dp)
        #     right_d=helper(i+1,j+1,dp)
        #     left_d=helper(i+1,j-1,dp)

        #     dp[i][j]=matrix[i][j]+min(down,right_d,left_d)
         
        #     return dp[i][j]
        # minVal=float('inf')
        # for j in range(n):
        #     minVal=min(minVal,helper(0,j,dp))
        # return minVal

        # Tabulation time:O(n^2) space:O(n^2)
        # dp=[[-1]*n for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         if i==0:dp[i][j]=matrix[i][j]
        #         else:
        #             down=dp[i-1][j]
        #             right_d=dp[i-1][j-1] if j>0 else float('inf')
        #             left_d=dp[i-1][j+1] if j<n-1 else float('inf')

        #             dp[i][j]=matrix[i][j]+min(down,right_d,left_d)
        # return min(dp[n-1])

        # tabulation time:O(n^2) space:O(n)
        prev=matrix[0]
        for i in range(1,n):
            curr=[-1]*n
            for j in range(n):
                down=prev[j]
                right_d=prev[j-1] if j>0 else float('inf')
                left_d=prev[j+1] if j<n-1 else float('inf')

                curr[j]=matrix[i][j]+min(down,right_d,left_d)
            prev=curr
        return min(prev)

