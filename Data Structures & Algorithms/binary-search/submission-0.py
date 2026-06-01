class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b = 0
        e = len(nums) - 1
        
        while b <= e:
            mi = b + (e - b)//2
            print("e",e,"b",b,"mi",mi, e-b,(e-b)//2 ,b + (e-b)//2)

            if nums[mi] == target:
                print("found at", mi)
                return mi
                        
            elif target < nums[mi]:
                e = mi - 1
            else:
                b = mi + 1


        return -1
            
        

