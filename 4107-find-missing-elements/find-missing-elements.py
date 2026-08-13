class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mi=min(nums)
        ma=max(nums)
        res=[]
        for i in range(mi,ma+1):
            if i not in nums:
                res.append(i)
        return res


