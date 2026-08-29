class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result=[]
    # TLE occured
        # def backtrack(first,result,nums):
        #     if first==n:
        #         result.append(nums[:])
        #         return 
        #     for i in range(n):
        #         nums[i],nums[first]=nums[first],nums[i]
        #         backtrack(first,result,nums)
        #         nums[i],nums[first]=nums[first],nums[i]
        # backtrack(0,result,nums)
        # return result
 # visited or not check
        curr=[]
        visited=[False]*n 
        def backtrack(result,nums,visited,curr):
            
            if len(curr)==n:
                result.append(curr[:])
                return 
            for i in range(n):
                if not visited[i]:
                    visited[i]=True
                    curr.append(nums[i])
                    backtrack(result,nums,visited,curr)
                    curr.pop()
                    visited[i]=False
        backtrack(result,nums,visited,curr)
        return result