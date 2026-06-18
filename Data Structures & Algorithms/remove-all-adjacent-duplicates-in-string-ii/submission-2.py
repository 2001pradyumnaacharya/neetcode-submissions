class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        m = []

        for i in s:
            if m and m[-1][0] == i:
                m[-1][1] +=1
            else:
                m.append([i,1])
            if m[-1][1] == k:
                m.pop()
        
        res = ''
        for k , v in m:
            res = res + (k*v)
        return res            

