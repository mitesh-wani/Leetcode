class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # nums.sort()
        # for i  in range(1,len(nums)):
        #     if nums[i]==nums[i-1]:
        #         return True 
        #         break
        # return False
        unique_list=set(nums)
        print(unique_list)
        if len(unique_list)==len(nums):
            return False
        else:
            return True