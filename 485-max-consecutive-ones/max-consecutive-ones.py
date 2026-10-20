class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        i,j=0,0
        n,ans=len(nums),0
        while j<n:
            if nums[j]==1:
                ans=max(ans,j-i+1)
                j+=1
            else:
                i=j+1
                j+=1
        return ans