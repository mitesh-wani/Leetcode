class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left<right:
            right=right&right-1
        return left & right

        
        cnt=0
        while left!=right:
            left=left>>1
            right=right>>1
            cnt+=1
        return left<<cnt

