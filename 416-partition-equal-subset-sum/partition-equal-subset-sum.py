class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        total=sum(nums)
        
        if total%2==1:return False
        target = total // 2
        ## recursion using dp matrix time:O(n*k) space:O(n*k+n)
        # dp=[[-1 for _ in range(target+1)] for _ in range(n)]
        # def subsetSum(i,k):
        #     if k==0:return True
        #     if i < 0 or k < 0: return False
        #     if i==0:
        #         if k==nums[i]:return True
        #         else:
        #             return False
        #     if dp[i][k]!=-1:return dp[i][k]
        #     not_pick=subsetSum(i-1,k)
        #     pick=False
        #     if nums[i]<=k:
        #         pick=subsetSum(i-1,k-nums[i])
        #     dp[i][k] = pick or not_pick
        #     return dp[i][k] 
        # return subsetSum(n-1,total//2)

# tabulation time:O(n*k) space:O(n*k)
        # dp=[[0 for _ in range(target+1)] for _ in range(n)]
        # for i in range(n):
        #     dp[i][0]=1
        # for j  in range(target):
        #     if j==nums[0]:
        #         dp[0][j]=1
        #     else:
        #         dp[0][j]=0
        # for i in range(1,n):
        #     for j in range(1,target+1):
        #         not_pick=dp[i-1][target]
        #         pick=0
        #         if nums[i]<=target:
        #             pick=dp[i-1][target-nums[i]]
        #         dp[i][target] = pick or not_pick
        # return bool(dp[n-1][target])
                    
# tabulation with space optimization time=O(n*k) space=(2*k)
        prev = [0] * (target + 1)
        prev[0] = 1
        if nums[0] <= target:
            prev[nums[0]] = 1

        
        for i in range(1,n):
            curr=[1]+[0]*(target)
            for j in range(1,target+1):
                not_pick=prev[j]
                pick=0
                if nums[i]<=j:
                    pick=prev[j-nums[i]]
                curr[j] = pick or not_pick
            prev=curr
        return bool(prev[target])
                
        