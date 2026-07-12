from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        g = []
        c = Counter(s)
        for l in order:
            if l in c:
               g.append(l * c[l])
               del c[l]
        for i , v in c.items():
            g.append(i * v)
        return "".join(g)