class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i , j = 0 , 0 
        s = ""

        while j < len(word2) or i < len(word1):
            if i < len(word1):
                s =  s + word1[i]
                print("added i")
            if j < len(word2):
                s =  s + word2[i]
                print("added j")

            
            i +=1
            j +=1
            print(s)
        return s