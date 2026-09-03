class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        for i in range(n-1,0,-1):
            avg=sum(nums[i:])/(n-i)
            if nums[i-1]>avg:
                count+=1
        return count

