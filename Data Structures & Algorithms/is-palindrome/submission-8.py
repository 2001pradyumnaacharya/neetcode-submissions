import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.replace(" ","").upper()
        x = ''.join(filter(lambda ch: ch not in string.punctuation, x))
        i , j = 0 , len(x) -1
        while i < j:
            if x[i] !=x[j]:
                return False
            i +=1
            j -=1
        return True