class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i , j = 0 ,1
        while i < len(nums) -1:
            if nums[i] == nums[j]:
                nums.pop(j)
                continue
            else:
                i +=1
                j +=1
        print(nums)
        return len(nums)