class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = len(nums)
        l , r = 0 , len(nums) - 1

        while l <= r:
            m = (l + r) //2

            if nums[m] == target:
                ans = m
                break
            elif nums[m] < target:
                l = m + 1
            else:
                ans = m 
                r = m -1
        return ans