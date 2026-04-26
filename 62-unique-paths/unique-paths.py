class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # base case and initialization same for all method
        i,j=m-1,n-1
        if i==0 or j==0:return 1
        # recrsive method time:O(2^m+n) space:O(m+n)
        
        # x=self.uniquePaths(i,j-1)
        # y=self.uniquePaths(i-1,j)
        # return x+y
        # memorizarion time:O(m*n) space:O(m+n+m*n)
        dp = [[-1] * n for _ in range(m)]
        def helper(i,j,dp):
            if i==0 or j==0:return 1
            if dp[i][j]!=-1:return dp[i][j]
            x=helper(i,j-1,dp)
            y=helper(i-1,j,dp)
            dp[i][j]=x+y
            return dp[i][j]
        return helper(i,j,dp)
        



