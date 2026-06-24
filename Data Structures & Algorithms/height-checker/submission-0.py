class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sh = sorted(heights)
        c = 0
        for e , p in zip(sh, heights):
            if e != p: 
                c +=1
        
        return c