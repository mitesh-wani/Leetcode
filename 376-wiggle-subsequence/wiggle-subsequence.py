class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        count=1
        n = len(nums)
        if n < 2:
            return n
        prev_diff=0
        for i in range(1,len(nums)):
            curr_diff=nums[i]-nums[i-1]
            if prev_diff<=0 and (curr_diff>0):
                prev_diff = curr_diff
                count+=1
            elif prev_diff>=0 and (curr_diff<0):
                count+=1
                prev_diff = curr_diff
        return count