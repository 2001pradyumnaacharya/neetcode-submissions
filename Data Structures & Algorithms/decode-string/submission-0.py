class Solution:
    def decodeString(self, s: str) -> str:
        g = []

        for i in s:
            if i != ']':
                g.append(i)
            else:

                sub = ''

                while g[-1] != '[':
                    sub = g.pop() + sub
                g.pop()

                d = ''

                while g and g[-1].isdigit():
                    d = g.pop() + d
                g.append(int(d) * sub)
                
        return ''.join(g)