class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        n=len(s1)
        s1_even=[]
        s1_odd=[]
        s2_even=[]
        s2_odd=[]
        for i in range(n):
            if i%2==0:
                s1_even.append(s1[i])
                s2_even.append(s2[i])
            else:
                s1_odd.append(s1[i])
                s2_odd.append(s2[i])
        
        if sorted(s1_even)==sorted(s2_even) and sorted(s1_odd)==sorted(s2_odd):
            return True
        else:
            return False

            
        