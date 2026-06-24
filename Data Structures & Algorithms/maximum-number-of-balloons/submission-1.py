class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        g = dict()
        for i in text:
            if i in g.keys() and i in "balloon":
                g[i] +=1
            elif i in "balloon":
                g[i] = 1

        if len(g) < 5:
            return 0

        g['l'] //=2
        g['o'] //=2
        return min(g.values())