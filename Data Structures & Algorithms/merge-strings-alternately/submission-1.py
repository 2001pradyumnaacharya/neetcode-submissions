class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        for i in range(max(len(word1),len(word2))):
            if i < len(word1):
                s = s + word1[i]
            if i < len(word2):
                s = s + word2[i]
            
        return s