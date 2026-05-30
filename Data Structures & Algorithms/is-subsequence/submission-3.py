class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        p = list(s)
        j = 0
        for i in t:
            if j < len(p) and i == p[j]:
                print(f"Incrimenting the thing as the {i , p[j]} so j is {j}")
                j +=1
        
        if j == len(p):
            return True
        else:
            return False