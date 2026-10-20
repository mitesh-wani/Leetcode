class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        i,j=0,0
        zeroes,ans=0,0
        arr=nums
        while j<len(arr):
            if arr[j]==0:
                zeroes+=1 
                while zeroes>k:
                    if arr[i]==0:
                        zeroes-=1
                    i+=1
            ans=max(ans,j-i+1)
            j+=1 
        return ans