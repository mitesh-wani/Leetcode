class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        

        s1_new=s1[2]+s1[3]+s1[0]+s1[1]
        s1_new2=s1[2]+s1[1]+s1[0]+s1[3]
        s1_new3=s1[0]+s1[3]+s1[2]+s1[1]
    
        if s1_new==s2 or s1==s2 or s2==s1_new2 or s2==s1_new3:
            return True
        else:
            return False