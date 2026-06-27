class Solution:
    def findLucky(self, arr: List[int]) -> int:
        g = dict()
        o = -1

        for i in arr:
            if i in g:
                g[i]+=1
            else:
                g[i] =1


        for k , v in g.items():
            if k == v:
                o= max(o,k) 

        return o
            