class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n=len(nums)
        res=[]
        # seq=[]
        # def Backtrack(i):
        #     if i>=n :
        #         # count  no subsequence that hav eless than or equal to targe with non-empty subsequence
        #         res.append(seq[:])
        #         return
            
        #     seq.append(nums[i])
        #     Backtrack(i+1)

        #     seq.pop()
        #     Backtrack(i+1)
        # Backtrack(0) 
        # return res
        nums.sort()
        mod=10**9 + 7
        count=0
        r=n-1
        l=0
        while l<=r:
            if nums[l]+nums[r]<=target:
                count+=pow(2,r-l,mod)
                l+=1
            else:
                r-=1
        return count%mod

            