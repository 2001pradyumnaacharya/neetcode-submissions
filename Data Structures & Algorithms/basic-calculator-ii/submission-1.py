class Solution:
    def calculate(self, s: str) -> int:
        op = '+'
        t = []
        num = 0
        s = s.replace(" ",'')
        for e, i in enumerate(s):
            if i.isdigit(): 
                num = num * 10 + int(i)
            if (not i.isdigit()) or e == len(s) -1:
                if op == '+':
                    t.append(num)
                elif op == '-':
                    t.append(-num)
                elif op == '*':
                    t[-1] *= num
                elif op == '/':
                    t[-1] = int(t[-1] / num)
                    
                op = i
                num = 0
            
        return sum(t)
         