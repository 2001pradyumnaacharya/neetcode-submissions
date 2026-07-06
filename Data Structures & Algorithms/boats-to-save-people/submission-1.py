class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        inb, l,r = 0,0,len(people) -1

        while l <=r:
            rem = limit - people[r]
            inb +=1
            r-=1
            if l <= r and rem >= people[l]:
                l+=1
        
        return inb
