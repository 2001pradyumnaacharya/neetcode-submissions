class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        print("The sprit s is ",s)

        s = s.split()

        return len(s[-1])
