class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # ans=0
        tree=fruits
        # typ1=[]
        # i,j=0,0
        # while j<len(tree):
        #     if tree[j]  in typ1:
        #         ans=max(ans,j-i+1)
        #         j+=1
        #     elif len(typ1)<2:
        #         typ1.append(tree[j])
        #     else:
        #         #print("inner",typ1)
        #         typ1=[]
        #         i+=1 
        #         j=i
        #     #print(typ1)
        # return ans 
        ans = 0
        count = collections.defaultdict(int)

        l = 0
        for r, t in enumerate(tree):
            count[t] += 1
            while len(count) > 2:
                count[tree[l]] -= 1
                if count[tree[l]] == 0:
                    del count[tree[l]]
                l += 1
            ans = max(ans, r - l + 1)

        return ans