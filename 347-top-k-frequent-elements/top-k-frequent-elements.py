class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq 
        m={}
        for a in nums:
            m[a]=m.get(a,0)+1 
        pq=[]
        for key,freq in m.items():
            heapq.heappush(pq,(freq,key))
            if len(pq)>k:
                heapq.heappop(pq)
            
        result=[]
        for freq, key in pq:
            result.append(key)
        return result