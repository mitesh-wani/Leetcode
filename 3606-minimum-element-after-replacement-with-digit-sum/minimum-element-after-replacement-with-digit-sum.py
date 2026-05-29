class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(num):
            ans=0
            while num!=0:
                ans+=num%10
                num=num//10
            return ans
        result=[]
        for num in nums:
            result.append(digit_sum(num))
        print(nums)
        return min(result)