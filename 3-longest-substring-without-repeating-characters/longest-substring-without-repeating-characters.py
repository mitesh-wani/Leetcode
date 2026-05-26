class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m={}
        n=len(s)
        i=0
        count=0
        for j in range(n):
            while s[j] in m:
                del m[s[i]]
                i+=1
            
            count=max(j-i+1,count)
            m[s[j]]=True
        return count