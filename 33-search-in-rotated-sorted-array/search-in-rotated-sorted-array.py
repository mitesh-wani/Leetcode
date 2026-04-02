class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans=-1
        low=0
        arr=nums
        high=len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]>=arr[low]:
                if arr[mid]>=target and arr[low]<=target:
                    high=mid-1
                else:
                    low=mid+1
            elif arr[mid]<=arr[high]:
                if arr[mid]<=target and arr[high]>=target:
                    low=mid+1
                else:
                    high=mid-1
        return -1



