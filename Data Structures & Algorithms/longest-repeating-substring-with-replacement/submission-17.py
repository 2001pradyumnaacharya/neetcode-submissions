from  itertools import groupby

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0 

        for c in set(s):
            count = l = 0

            for i in range(len(s)):

                if s[i] == c:
                    count +=1
                
                while (i - l + 1) - count > k:
                    if s[l] == c:
                        count -=1
                    l +=1 
                ans = max(ans, i - l +1)

        return ans


        