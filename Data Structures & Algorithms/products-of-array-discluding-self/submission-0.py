import numpy as np
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        d = {}
        temp = []
        for i, e in enumerate(nums):
            new_list = nums[:i] + nums[i + 1:]
            d[i] = new_list

        print(nums)
        print(d)

        for k ,v in d.items():
            temp.append(math.prod(np.array(v)))

        return temp