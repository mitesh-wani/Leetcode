class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        subsetArr=[]
        res=[]
        def AddSubset(i):
            if i>=n:
                res.append(list(subsetArr))
                return
            subsetArr.append(nums[i])
            AddSubset(i+1)
            subsetArr.pop()
            AddSubset(i+1)
        AddSubset(0)
        return res