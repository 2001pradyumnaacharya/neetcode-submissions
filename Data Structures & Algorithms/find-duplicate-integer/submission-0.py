class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = set()
        for i in nums:
            if i not in temp:
                temp.add(i)
            else:
                return i
        
        return 0
