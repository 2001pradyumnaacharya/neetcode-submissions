class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()

        for i , c in enumerate(nums):

            if c in seen and i - seen[c] <= k:
                return True

            seen[c] = i

        return False

            