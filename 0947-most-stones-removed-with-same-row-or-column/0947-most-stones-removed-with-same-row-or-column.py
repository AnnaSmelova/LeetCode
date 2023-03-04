class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        h=defaultdict(list)
        v=defaultdict(list)
        for i, s in enumerate(stones):
            h[s[0]].append(i)
            v[s[1]].append(i)
        l=len(stones)
        g=[[] for i in range(l)]
        vlist=[0]*l
        for i, s in enumerate(stones):
            g[i]+=[j for j in h[s[0]] if j!=i]
            g[i]+=[j for j in v[s[1]] if j!=i]
        ans=l
        for i in range(l):
            if not vlist[i]:
                vlist[i]=1
                ans-=1
                q=[i]
                curs=0
                while curs<len(q):
                    tmp=q[curs]
                    for j in g[tmp]:
                        if not vlist[j]:
                            vlist[j]=1
                            q.append(j)
                    curs+=1
        return ans
        