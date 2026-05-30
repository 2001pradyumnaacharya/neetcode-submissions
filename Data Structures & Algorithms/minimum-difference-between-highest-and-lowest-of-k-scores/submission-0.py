class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        i, j = 0 , k -1
        r = 0
        nums.sort()
        while j < len(nums):
            s = nums[j] - nums[i] 
            if r == 0:
                r = s
                print(f"The r was 0 so i want {r}")
            else:

                r = min(r, s)
                print(f"r is set to min so r is {r} by sub {nums[j] , nums[i] }")
            
            i +=1
            j +=1
        
        return r