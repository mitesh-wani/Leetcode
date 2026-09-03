class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #nums.sort()
        count=0
        n=len(nums)
        if n<=1:
            return n
        ans=0
        # for i  in range(n-1):
        #     if nums[i+1]-nums[i]==1:
        #         count+=1
        #     elif nums[i+1]==nums[i]:
        #         continue
        #     else:
        #         count=0 
        #     ans=max(count,ans)
        s=set(nums)
        for x in s:
            if x-1 not in s:
                count=1
                nextval=x+1
                while nextval in s:
                    count+=1
                    nextval+=1
                ans=max(ans,count)
        return ans