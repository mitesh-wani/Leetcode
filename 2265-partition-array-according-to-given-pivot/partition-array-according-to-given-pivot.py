class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        if n==0 or n==1:
            return nums
        
        less,equal,greater=0,0,0
         
        for i in range(n):
            if nums[i]<pivot:
                less+=1
            elif nums[i]==pivot:
                equal+=1
            elif nums[i]>pivot:
                greater+=1
        left=0
        mid=less
        right=less+equal
        result=[float('inf')]*n
        for i in range(n):
            if nums[i]<pivot:
                result[left]=nums[i]
                left+=1
            elif nums[i]==pivot:
                result[mid]=nums[i]
                mid+=1
            elif nums[i]>pivot:
                result[right]=nums[i]
                right+=1

        return result

