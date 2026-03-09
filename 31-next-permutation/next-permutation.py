class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        ind=-1
        for i in range(n-2,-1,-1):
            print(i)
            if nums[i]<nums[i+1]:
                ind=i
                break
        
        if(ind==-1):
            nums.reverse()
        else:
            for j in range(n-1,ind,-1):
                if(nums[j]>nums[ind]):
                    temp=nums[ind]
                    nums[ind]=nums[j]
                    nums[j]=temp
                    break
            nums[ind+1:]=reversed(nums[ind+1:])