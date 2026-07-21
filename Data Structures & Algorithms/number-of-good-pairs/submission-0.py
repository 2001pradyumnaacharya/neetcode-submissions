class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = Counter(nums)
        res = 0
        for num, c in d.items():
            res += c * (c - 1) // 2
        return res
