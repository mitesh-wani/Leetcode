class Solution:
    def frequencySort(self, s: str) -> str:
        m={}
        for i in s:
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
        sort_m=sorted(m,key=m.get,reverse=True)
        res=""
        for i in sort_m:
            res+=(i*m[i])
       
        return res