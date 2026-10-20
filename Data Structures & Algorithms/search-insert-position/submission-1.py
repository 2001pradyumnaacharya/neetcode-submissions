class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = len(nums)
        l , r = 0 , len(nums) - 1

        while l <= r:
            m = (l + r) //2

            if nums[m] == target:
                ans = m
                print("found it ", nums[m], m)
                break
            elif nums[m] < target:
                l = m + 1
                print("changing l ", l ,"and m is", nums[m])
            else:
                ans = m 
                r = m -1
                print("changeing r ", l ,"and m is", nums[m])
            print(ans)
        return ans