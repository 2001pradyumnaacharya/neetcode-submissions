class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        i_right = True
        for i in range(1,len(nums)):
            if nums[i-1] % 2 == 0 and nums[i] %2 == 0:
                i_right = False
            elif nums[i-1] % 2 != 0 and nums[i] %2 != 0:
                i_right = False

        return i_right