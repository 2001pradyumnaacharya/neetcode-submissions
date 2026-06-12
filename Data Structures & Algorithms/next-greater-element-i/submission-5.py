class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            nl = -1
            print("Indec",nums2[index:])
            for j in nums2[index:]:
                if j > nums1[i]:
                    nl = j
                    break
            nums1[i] = nl
        print(nums1)
        return nums1


        