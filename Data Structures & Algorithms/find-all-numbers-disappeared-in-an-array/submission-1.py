class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ar = []

        for i in range(1, len(nums)+1):
            if not i in nums:
                ar.append(i)

        return ar