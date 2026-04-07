import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_to_Eat(speed):
            totalTime=0
            for p in piles:
                totalTime+=math.ceil(p/speed)
            return totalTime
        
        low =1 
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            if mid==0:
                low=1
                continue
            if time_to_Eat(mid)<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans