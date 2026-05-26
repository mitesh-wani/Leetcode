class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        note={}
        for i in word:
            if i.islower():
                note[i]=False
        for i in word:
            if i.isupper():
                if i.lower() in note:
                    note[i.lower()]=True
        for key,val in note.items():
            if val==True:
                count+=1
        return count
        