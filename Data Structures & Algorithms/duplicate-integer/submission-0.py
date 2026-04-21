class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        try:
            sett = set(nums)
            if len(sett)!=len(nums):
                return True
            else:
                return False
        except Exception as e:
            print(e)