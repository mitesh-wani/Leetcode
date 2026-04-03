class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1
        ans=float('inf')
        while low<=high:
            mid=low+(high-low)//2
            if nums[low]<=nums[mid]:
                ans =min(ans,nums[low])
                low=mid+1
            elif nums[high]>=nums[mid]:
                ans=min(ans,nums[mid])
                high=mid-1
        return ans  