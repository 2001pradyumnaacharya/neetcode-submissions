class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                else:
                    if words[i] in words[j] and words[i] not in s:
                        s.append(words[i])

            print(words[i], s)
        return s