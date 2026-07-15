class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = dict()

        for w in words:
            for c in w:
                if c in d:
                    d[c] +=1
                else:
                    d[c] = 1
                

        for c in d.values():
            if c % len(words):
                return False
        return True