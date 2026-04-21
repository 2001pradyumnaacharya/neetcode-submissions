class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tt = list(t)
        ss = list(s)

        if len(s)!= len(t):
            return False


        for i in ss:
          if i in tt:
            tt.remove(i)

        

        if len(tt)!= 0:
            return False
        else:
            return True