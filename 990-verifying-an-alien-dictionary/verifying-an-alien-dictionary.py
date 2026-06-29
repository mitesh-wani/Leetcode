from collections import deque
class Solution:
# You only need to check whether the words are already sorted according to order.
# You do not need to build a graph or perform topological sort.
    # def topologicalSort(self,adj,unique_char):
    #     ans=[]
    #     q=deque()
    #     indegree={char:0 for char in adj}
    #     for i in adj:
    #         for k in adj[i]:
    #             indegree[k]+=1
    #     for c in unique_char:
    #         if indegree[c]==0:
    #             q.append(c)
    #     while q:
    #         node=q.popleft()
    #         ans.append(node)
    #         for k in adj[node]:
    #             if k in indegree:
    #                 indegree[k]-=1 
    #                 if indegree[k]==0:
    #                     q.append(k)
    #     return ans 

    # def isAlienSorted(self, words: List[str], order: str) -> bool:
    #     unique_char=set("".join(words))
    #     adj={char:[] for char in unique_char}
    #     for i in range(len(words)-1):
    #         w1=words[i]
    #         w2=words[i+1]
    #         if len(w1)>len(w2) and w1.startswith(w2):
    #             return False
    #         length=min(len(w1),len(w2))
    #         for j in range(length):
    #             if w1[j]!=w2[j]:
    #                 adj[w1[j]].append(w2[j])
    #                 break 
    #     v=self.topologicalSort(adj,unique_char) 
    #     if len(v)!=len(unique_char):
    #         return False
    #     order_map={char:index for index,char in enumerate(order)}
    #     for i in range(len(v)-1):
    #         if order_map[v[i]]>order_map[v[i+1]]:
    #             return False
    #     return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        adj={char:idx for idx,char in enumerate(order)}
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            length=min(len(w1),len(w2))
            for j in range(length):
                if w1[j]!=w2[j]:
                    if adj[w1[j]]>adj[w2[j]]:
                        return False
                    break
            else:
                if len(w1)>len(w2):
                    return False
        return True 
