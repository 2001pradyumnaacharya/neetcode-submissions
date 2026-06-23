class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        mi = 0
        g = dict()
        du = 0
        cnt = 0
        for sl in grid:
            for i in sl:
                cnt +=1
                if i in g.keys():
                    g[i]+=1
                    if g[i] == 2:
                        du = i
                else:
                    g[i] = 1

        for i in range(1,cnt+1):
            if i not in g.keys():
                mi = i
        return [du, mi]

        

        