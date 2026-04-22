class Solution:
    def rob(self, nums: List[int]) -> int:
        # # memorization
        # n=len(nums)
        # if n == 0: return 0
        # if n == 1: return nums[0]
        # dp=[-1]*n
        # def houseRobberI(i,arr,dp): 
        #     # base case
        #     if i==0: 
        #         return arr[0]
        #     if i<0: 
        #         return 0
        #     if dp[i]!=-1:
        #         return dp[i]
        #     pick=arr[i]+houseRobberI(i-2,arr,dp)
        #     not_pick=0+houseRobberI(i-1,arr,dp)
        #     dp[i]=max(pick,not_pick)
        #     return dp[i]
        # return houseRobberI(n-1,nums,dp)

        #Tabulation
        n=len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        dp=[-1]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            pick=nums[i]+dp[i-2]
            not_pick=0+dp[i-1]
            dp[i]=max(pick,not_pick)
        return dp[n-1]