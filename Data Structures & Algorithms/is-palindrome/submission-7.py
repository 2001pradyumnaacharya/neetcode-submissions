import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.replace(" ","").upper()
        x = ''.join(filter(lambda ch: ch not in string.punctuation, x))
        # print("fffff",str(c))
        print('ggg',x)
        print(len(x),len(x)/2)
        print(len(x)-1)
        print(string.punctuation)
        for i in range(int(len(x)/2)):
            if x[i] != x[(len(x)-1) - i]:
                print(x[i], x[(len(x)-1) - i])
                return False
        return True