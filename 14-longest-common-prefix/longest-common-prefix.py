class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_str=""
        k=0
        word=strs
        n=len(strs)
        if n==0:return ""
        if n==1:return word[0]

        while True:
            for i in range(n):
                if k==len(word[i]):return word[0][:k]
                if word[i][k]!=word[0][k]:return word[0][:k]
            k+=1    
        return ""