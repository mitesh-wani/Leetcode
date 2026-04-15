class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        min_dist=float('inf')
        n=len(words)
        for i in range(n):
            if words[i]==target:
                idx=i
                right_dist=abs(i-startIndex)
                left_dist=n-right_dist
                min_dist=min(min_dist,left_dist,right_dist)
        return -1 if min_dist==float('inf') else min_dist