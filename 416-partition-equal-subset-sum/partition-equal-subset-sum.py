class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        total=sum(nums)
        
        if total%2==1:return False
        target = total // 2
        dp=[[-1 for _ in range(target+1)] for _ in range(n)]
        def subsetSum(i,k):
            if k==0:return True
            if i < 0 or k < 0: return False
            if i==0:
                if k==nums[i]:return True
                else:
                    return False
            if dp[i][k]!=-1:return dp[i][k]
            not_pick=subsetSum(i-1,k)
            pick=False
            if nums[i]<=k:
                pick=subsetSum(i-1,k-nums[i])
            dp[i][k] = pick or not_pick
            return dp[i][k] 
        return subsetSum(n-1,total//2)