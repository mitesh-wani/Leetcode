class Solution:
    def maxJump(self, stones: List[int]) -> int:
        # n=len(stones)
        # dp=[-1]*n
        # def measures(stones,i,dp):
        #     if i==0:
        #         return 0
        #     if dp[i]!=-1:
        #         return dp[i]
        #     min_length=float('inf')
        #     for j in range(1,n):
        #         if i-j>=0:
        #             length=abs(stones[i]-stones[j])+measures(stones,i-j,dp)
        #             min_length=min(length,min_length)
        #     dp[i]=min_length
        #     return min_length
        # measures(stones,n-1,dp)
        # print(dp)
        # return max(dp)
        if len(stones) == 2:
            return stones[1] - stones[0]
        ans = stones[1] - stones[0]
        for i in range(2, len(stones)):
            ans = max(ans, stones[i] - stones[i - 2])
            
        return ans