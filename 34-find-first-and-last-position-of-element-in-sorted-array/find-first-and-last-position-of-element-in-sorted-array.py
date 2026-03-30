class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: # Quick exit for empty lists
            return [-1, -1]
        lower_bound_idx = bisect.bisect_left(nums, target)
        
        # Check if index is in bounds AND points to the target
        if lower_bound_idx < len(nums) and nums[lower_bound_idx] == target:
            upper_bound_idx = bisect.bisect_right(nums, target)
            return [lower_bound_idx, upper_bound_idx - 1]
        
        return [-1, -1]
        # first_index=-1
        # last_index=-1
        # low,high=0,len(nums)-1
        # while low <=high:
        #     mid=low+(high-low)//2
        #     if nums[mid]==target:
        #         first_index=mid
                
        #     elif nums[mid]>target:
        #         low=mid+1
        #     else:
        #         high=mid-1
        # while low <=high:
        #     mid=low+(high-low)//2
        #     if nums[mid]==target:
        #         last_index=mid
        #     elif nums[mid]<target:
        #         low=mid+1
        #     else:
        #         high=mid-1
        # return [first_index,last_index]




            