class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for n in queries:
            c = 0
            for w in words[n[0]:n[1]+1]:
                if w[0] in ['a', 'e', 'i', 'o','u'] and w[-1] in ['a', 'e', 'i', 'o','u']:
                    c +=1
            ans.append(c)
        return ans
