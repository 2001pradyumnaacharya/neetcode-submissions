class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        h = dict()
        t = []
        for i in arr:
            if i in h:
                h[i]+=1
            else:
                h[i] = 1
        for p , v in h.items():
            if v ==1:
                t.append(p)
        if len(t) >= k:
            return t[k-1]
        return ""
            