class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        g = dict()
        par = len(nums)//2
        for i in nums:
            if i in g.keys():
                g[i]+=1
                if g[i] >= 2 and par >0:
                    par-=1
                    g.pop(i)
                    print("reducint the par", par)
            else:
                g[i] = 1
        print(g)
        if par == 0:
            return True
        else:
            return False

            
        
