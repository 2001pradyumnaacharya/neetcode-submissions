class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i , j = 0 , k -1
        d = []
        while j < len(arr):
            if sum(arr[i:j + 1]) / k >= threshold:
                d.append(arr[i:j + 1])
            i +=1
            j +=1
        return len(d)