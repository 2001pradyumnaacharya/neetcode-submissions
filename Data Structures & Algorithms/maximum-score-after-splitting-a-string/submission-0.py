class Solution:
    def maxScore(self, s: str) -> int:
        i , j = 0 , 1
        ans = []
        z= 0
        o = 0 

        while i < len(s) - 1:
            if int(s[i]) == 0:
                z +=1
            while j < len(s):
                if int(s[j]) == 1:
                    o +=1
                j +=1
            print( "noo is ",z,"and se1 is", o)
            ans.append(z + o)
            o = 0
            i +=1
            j = i +1

        return max(ans)
            