
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = groupby(nums)
        tempo = {}
        for i in group:
            # print(i[0],list(i[1]))
            if i[0] in tempo.keys():
                tempo[i[0]] +=  len(list(i[1]))
            else:
                tempo[i[0]] = len(list(i[1]))
        print(tempo)
       
        tu = sorted(tempo.values(), reverse = True)

        t = []

        for i, v in tempo.items():
            if v in tu[0:k]:
                t.append(i)
        return t