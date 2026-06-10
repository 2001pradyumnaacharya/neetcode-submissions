class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        d = dict()
        n = len(nums) // 2

        for i in nums:
            if i in d:
                d[i]+=1
                if d[i] > n:
                    return i
            else:
                d[i] = 1
        
        return 0