class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for q in queries:
            l,r,k,v=q[0],q[1],q[2],q[3]
            idx =l
            while idx<=r:
                nums[idx]=(nums[idx]*v)%(1000000007)
                idx+=k
        xor=0
        for i in nums:
            xor^=i
        return xor