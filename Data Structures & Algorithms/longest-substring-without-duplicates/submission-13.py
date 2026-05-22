class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        d = [s[0]]
        j = 1
        ans = 1

        while j < len(s):

            if s[j] not in d:
                d.append(s[j])

            else:
                while s[j] in d:
                    d.pop(0)

                d.append(s[j])

            ans = max(ans, len(d))
            j += 1

        return ans