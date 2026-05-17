class Solution:
    def isValid(self, s: str) -> bool:
        validater = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        temp = []
        for c in s:
            
            if c in validater:
                if temp and temp[-1] == validater[c]:
                    temp.pop()
                else:
                    return False
            else:
                temp.append(c)

        return True if not temp else False