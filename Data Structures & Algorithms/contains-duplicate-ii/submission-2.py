class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i , j = 0, 1
        if len(nums) == 1:
            return False
        while i < len(nums) -1:
            if nums[i] == nums[j] and (j - i) <= k and i != j:
                print(f"The i and j {i,i} in {nums[i] ,nums[j]}")
                return True
            if j < len(nums) - 1:
                j +=1
            else:
                i +=1
                j = i+1
        return False

            