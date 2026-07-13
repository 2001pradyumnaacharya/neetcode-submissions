class Solution:
    def minOperations(self, s: str) -> int:
        res = 0
        s = list(s)
        for i in range(len(s)):
            if i == 0:
                continue
            else:
                if s[i-1] == s[i]:
                    if s[i-1] == "0":
                        s[i] = "1"
                    else:
                        s[i] = "0"
                    res +=1
        return min(res , len(s) -res)