class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n=len(triangle)
        # recursion time:O(n^2/n) space:O(2*n)
        # def helper(i,j):
        #     if i==n-1:return triangle[n-1][j]

        #     diagonal=triangle[i][j]+helper(i+1,j+1)
        #     down=triangle[i][j]+helper(i+1,j)
        #     return min(diagonal,down)
        
        # return helper(0,0)
        # memorization time:O(n^2/2) space:O(n+n^2) have n stack space
        # dp=[[-1]*n for _ in range(n)]
        # def helper(i,j):
        #     if i==n-1:return triangle[n-1][j]
        #     if dp[i][j]!=-1:return dp[i][j]
        #     diagonal=triangle[i][j]+helper(i+1,j+1)
        #     down=triangle[i][j]+helper(i+1,j)
        #     dp[i][j]=min(diagonal,down)
        #     return dp[i][j]
        
        # return helper(0,0)
        #tabulation time:O(n^2) space:O(n^2)
        # dp=[[-1]*n for _ in range(n)]
        # for j in range(n):
        #     dp[n-1][j]=triangle[n-1][j]
        # for i in range(n-2,-1,-1):
        #     for j in  range(i+1):
        #         down=triangle[i][j]+dp[i+1][j]
        #         diagonal= triangle[i][j]+dp[i+1][j+1]
        #         dp[i][j]=min(down,diagonal)
        # return dp[0][0]

        # tabulation with space:O(n)
        prior=[-1]*n
        curr=[-1]*n
        for j in range(n):
            prior[j]=triangle[n-1][j]
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                down=triangle[i][j]+prior[j]
                diagonal= triangle[i][j]+prior[j+1]
                curr[j]=min(down,diagonal)
            prior=curr[:]
        return prior[0]
