class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = []

        for i in range(len(temperatures)):
            count = 0
            j = i + 1
            r = []
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    r.append(count + 1)
                    temp = temp + r
                    print("Append :",temp)
                    break
                else: 
                    count+=1
                    j +=1
                    continue
            if not r:
                r.append(0)
                temp = temp + r
            
                
        return temp
