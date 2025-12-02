class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod=10**9+7
        from collections import Counter
        cnt=Counter()
        for x,y in points:
            cnt[y]+=1
        a=[]
        for v in cnt.values():
            if v>=2:
                a.append(v*(v-1)//2)
        s=sum(a)
        s2=sum(x*x for x in a)
        ans=((s*s - s2)//2) % mod
        return ans