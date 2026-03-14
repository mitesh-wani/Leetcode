class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        karr=[]
        n=len(nums)
        if n == 0: return nums
        k = k % n
        k=n-k
        for i in range(k):
            karr.append(nums[i])
        for j in range(k,n):
            nums[j-k]=nums[j]
        for i in range(n-k,n):
            nums[i]=karr[i-(n-k)]
        