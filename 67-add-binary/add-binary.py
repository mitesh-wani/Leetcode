class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        carry=0
        res=""
        while i>=0 or j>=0 or carry:
            bit1=int(a[i]) if i>=0 else 0
            bit2=int(b[j]) if j>=0 else 0
            sum=bit1+bit2+carry
            carry=sum//2
            ans=sum%2 
            res=str(ans)+res 
            i-=1
            j-=1
        return res