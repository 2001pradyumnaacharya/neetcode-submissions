class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = []
        i, j = 0, len(heights) - 1

        while i < j:
            print( " value in I ",heights[i], " value in J ",heights[j]," len: ", len(heights[i:j]))
            print(len(heights[i:j]) * min(heights[i], heights[j]))
            res.append(len(heights[i:j]) * min(heights[i], heights[j]))
            if heights[i] < heights[j]:
                i +=1
            else:
                j -=1

        return max(res)