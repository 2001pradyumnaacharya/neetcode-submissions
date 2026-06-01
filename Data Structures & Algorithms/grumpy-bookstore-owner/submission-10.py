class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        normal_cust = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                normal_cust  +=customers[i]
        print(normal_cust)
        i = j = 0 
        maxi = 0
        c= 0
        while j < len(customers):
            if grumpy[j] == 1:
                c +=customers[j]
                # print("the c is", c, "after addding", customers[j])

            if len(customers[i:j +1]) == minutes:
                # print("length of the len(customers[i:j]) reached ", len(customers[i:j]))
                maxi = max(maxi, c)
                # print("Setting max too", maxi)
                i +=1
                j = i
                c =0
            else:
                j +=1
        return normal_cust + maxi