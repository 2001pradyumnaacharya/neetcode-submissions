class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for r in range(len(nums)):
            if nums[r] == 0:
                l = r
                while nums[l] == 0 and l < len(nums) - 1:
                    l +=1
                nums[r] , nums[l] = nums[l] , nums[r]
        
        return nums
        
