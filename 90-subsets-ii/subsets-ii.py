class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res=[]
        n=len(nums)
        subset=[]
        def addSubset(i):
            if i>=n:
                res.append(list(subset))
                return

            subset.append(nums[i])
            addSubset(i+1)

            subset.pop()
            while i+1<n and nums[i]==nums[i+1]:
                i+=1
            addSubset(i+1)
        addSubset(0)
        return res

