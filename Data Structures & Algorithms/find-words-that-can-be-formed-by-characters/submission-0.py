class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        source = Counter(chars)
        for i in words:
            w = Counter(i)
            if len(w - source) == 0:
                res+=len(i)
        
        return res