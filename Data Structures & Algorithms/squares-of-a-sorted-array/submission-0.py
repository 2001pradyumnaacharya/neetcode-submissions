class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp = []

        for i in range(len(nums)):
            if i == 0:
                temp.append(nums[i]**2)
            else:
                temp.append(nums[i]**2)
                j = len(temp) -1
                while j > 0 and temp[j-1] >= temp[j]:
                    temp[j-1] , temp[j] = temp[j] , temp[j-1]
                    j -=1
            
        return temp

        

        