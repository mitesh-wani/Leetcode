class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        sum_val=0
        m={}
        for i in range(len(nums)):
            sum_val+=nums[i]
            if sum_val==k:
                count+=1
            if sum_val-k in m:
                count+=m[sum_val - k]
    
            m[sum_val] = m.get(sum_val, 0) + 1
        return count