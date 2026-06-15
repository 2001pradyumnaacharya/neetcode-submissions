class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = []

        for i in logs:
            if s and i == "../":
                s.pop()
            elif i not in ["../","./"]:
                s.append(i)

        return len(s)
            