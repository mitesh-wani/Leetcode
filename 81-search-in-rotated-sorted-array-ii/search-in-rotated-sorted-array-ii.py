class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low,high=0,len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return True
            if nums!=target and(nums[mid]==nums[low] and nums[high]==nums[mid]):
                low+=1
                high-=1 
            elif nums[low]<=nums[mid]:
                if target<=nums[mid] and target>=nums[low]:
                    high=mid-1
                else:
                    low=mid+1
            elif nums[high]>=nums[mid]:
                if target<=nums[high] and target>=nums[mid]:
                    low=mid+1
                else:
                    high=mid-1
        return False
                    