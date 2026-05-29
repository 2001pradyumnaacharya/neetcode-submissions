class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i , j = 0, 1

        while i < len(arr):
            
            while j< len(arr):
                if arr[j] > arr[i]:
                    print(f"I have the to replace {arr[i]} with {arr[j]} where i is {i}")
                    arr[i] = arr[j]
                    noc = arr[i]
                    j +=1
                else:
                    print(f"Passing Through because i {arr[i]} not > {arr[j]}")
                    j +=1
            i +=1
            j = i + 1
        arr.pop(0)
        arr.append(-1)
        print(arr)
        return arr
