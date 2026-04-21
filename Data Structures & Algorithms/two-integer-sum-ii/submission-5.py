class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        t  = dict()

        for i , v in enumerate(numbers):
            t[v] = i
        print(t)
        for i , v in enumerate(numbers):
            if target - v   in t.keys():
               return [min(i,t[target - v])+1, max([i,t[target - v]])+1]

        return []