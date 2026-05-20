class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t = []
        car = [[p,s] for  p,s in zip(position,speed)]
        print(car)
        
        for p, s in sorted(car)[::-1]:
            t.append((target - p)/s)
            if len(t)>=2 and t[-1] <= t[-2]:
                t.pop()

        return len(t)