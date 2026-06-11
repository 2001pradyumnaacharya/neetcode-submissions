class Solution:
    def maxDifference(self, s: str) -> int:
        d  = dict()
        odd = 1 
        even = 100
        for i in s:   
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        
        for k , v in d.items():
            if v % 2 !=0:
                odd = max(odd,v)
            else:
                even = min(even,v)
        return odd - even