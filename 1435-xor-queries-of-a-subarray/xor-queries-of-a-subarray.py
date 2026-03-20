class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result=[]
        # for a in queries:
        #     xor=0
        #     for i in range(a[0],a[1]+1):
        #         xor^=arr[i]
            
        #     result.append(xor)
        for i in range(1,len(arr)):
            arr[i]^=arr[i-1]
        for l,r in queries:
            if l==0:
                result.append(arr[r])
            else:
                result.append(arr[r]^arr[l-1])
        return result