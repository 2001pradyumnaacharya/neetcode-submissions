class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if s.strip() == "" or t.strip() == "":
            return 0
        
        j = 0
        for r in s:
            if j < len(t) and r == t[j]:
                j +=1
        
        return len(t[j:])