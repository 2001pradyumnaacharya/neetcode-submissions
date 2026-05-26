from collections import Counter
from typing import List
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) or not s1.strip() or not s2.strip():
            return False

        i , j  = 0 , len(s1) - 1

        while j < len(s2):
            if Counter(list(s1)) == Counter(list(s2[i:j+1])):
                return True
            else:
                i +=1
                j +=1
            
        return False


