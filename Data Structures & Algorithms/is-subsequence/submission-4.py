class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        j = 0
        for i in t:
            if j < len(s) and i == s[j]:
                print(f"Incrimenting the thing as the {i , s[j]} so j is {j}")
                j +=1
        
        if j == len(s):
            return True
        else:
            return False