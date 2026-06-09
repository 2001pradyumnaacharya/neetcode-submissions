class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapT, mapS = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if((c1 in mapT and mapT[c1]!=c2) or (c2 in mapS and mapS[c2] != c1)):
                return False
            mapT[c1] = c2
            mapS[c2] = c1

        return True