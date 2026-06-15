class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []

        for i in operations:
            if i in ['+','D','C'] and s:
                if i == "+" and len(s) >= 2:
                    s.append(s[-1]+s[-2])
                elif i == "C" and s:
                    s.pop()
                elif i == "D" and len(s) >= 1:
                    s.append(s[-1]*2)
            else:
                s.append(int(i))

        return sum(s)