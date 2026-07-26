class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    # recursion O(n^amount)
        #dp=[-2]*(amount+1)
        # def helper(coins,balance):
        #     if balance==0:return 0
        #     if balance <0:return -1
        #     mini=float('inf')
        #     for c in coins:
        #         count=helper(coins,balance-c)
        #         if count !=-1:
        #             mini=min(mini,1+count)
        #     if mini ==float('inf'):
        #         return -1
        #     else:
        #         return mini
        # return helper(coins,amount)
    # recursion with memorization O(amount*n)
        # dp=[-2]*(amount+1)
        # def helper(coins,balance,dp):
        #     if balance==0:return 0
        #     if balance <0:return -1
        #     if dp[balance]!=-2:
        #         return dp[balance]
        #     mini=float('inf')
        #     for c in coins:
        #         count=helper(coins,balance-c,dp)
        #         if count !=-1:
        #             mini=min(mini,1+count)
        #     dp[balance]= mini if mini !=float('inf') else -1
        #     return dp[balance]
        # return helper(coins,amount,dp)
    # bottom up approach using dp
        dp=[0]*(amount+1)
        dp[0]=0
        for a in range(1,amount+1):
            mini=float('inf')
            for c in coins:
                if a-c>=0 and dp[a-c]!=-1:
                    mini=min(mini,1+dp[a-c])
            dp[a]=mini if mini!=float('inf') else -1
        return dp[amount]