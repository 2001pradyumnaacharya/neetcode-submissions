class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        r = []
        
        # print('start of the ',temp, t[0])
        
        for e, i in enumerate(sorted(set(nums))):
            if e == 0:
                temp = [i]
            if i + 1 in nums :
                print('i before adding',i, 'i after adding', i+1)
                print('adding : ', i+1, "to temp.")
                temp.append(i+1)
                print(temp)
                print('r, ',r)
            else:
                print('entred else,' , r)
                r.append(len(temp))
                temp = [i+1]
        r.append(len(temp))

        print(r)
                
        return max(r)
        