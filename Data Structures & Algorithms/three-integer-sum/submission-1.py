from itertools import permutations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i , v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue

            k,j = i+1, len(nums)-1

            while k < j:
                s = v + nums[k] +   nums[j]
                if s > 0:
                    j -=1
                elif s < 0:
                    k +=1
                else:
                    res.append([v, nums[k] ,  nums[j]])
                    k += 1
                    j -= 1
                    while nums[k] == nums[k -1] and k < j:
                        k +=1

        return res
