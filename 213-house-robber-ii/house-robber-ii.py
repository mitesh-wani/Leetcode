class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=0:return 0
        if n==1:return nums[0]

        def houseRob(arr):
            prev1,prev2=0,0
            for h in arr:
                curr=max(prev1,h+prev2)
                prev2=prev1
                prev1=curr
            return prev1
        return max(houseRob(nums[:-1]),houseRob(nums[1:]))