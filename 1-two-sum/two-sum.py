class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        """
        # arr=sorted(nums)
        # right=len(nums)-1
        # left=0
        # add=0
        
        # while right>=left:
        #     add=arr[right]+arr[left]
        #     if(add==target):
        #         if(nums.index(arr[left])==nums.index(arr[right])):
        #             return nums.index(arr[left]),arr.index(arr[right])+1
        #         else:
        #             return nums.index(arr[left]),nums.index(arr[right])
        #     elif(add>target):
        #         right-=1
        #     elif(target>add):
        #         left+=1
        know={}
        for i,num in enumerate(nums):
            need=target-num
            if(need in know):
                return [know[need],i]
            know[num]=i
        