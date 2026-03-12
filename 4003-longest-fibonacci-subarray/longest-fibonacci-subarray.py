class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n <= 2:
            return n

        max_length=0
        curr_length=2
        
        for i in range(2,n):
            if nums[i-1]+nums[i-2]==nums[i]:
                curr_length+=1
                max_length=max(max_length,curr_length)
            else:
                curr_length=2
        return max_length if max_length>=3 else 2
