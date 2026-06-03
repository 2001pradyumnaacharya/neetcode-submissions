class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            ans += max(ord(s[i]),ord(s[i-1])) - min(ord(s[i]),ord(s[i-1]))

        return ans