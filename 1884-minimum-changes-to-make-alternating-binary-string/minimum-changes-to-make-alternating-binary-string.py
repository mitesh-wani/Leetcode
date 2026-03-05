class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=list(s)
        n=len(s)
        count1=0
        for i in range(1,n):
            if s[i-1]==s[i]:
                count1+=1
                if s[i]=='0':
                    s[i]='1'
                else:
                    s[i]='0'
        print(s)
        

        return min(count1,n-count1)
        