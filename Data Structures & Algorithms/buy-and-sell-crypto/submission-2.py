class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = [0]
        i , j = 0 , 1

        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
                j +=1
                print("jjjjjjjjjjjjjj")
                continue
            
            if prices[i] < prices[j]:
                max_price = prices[j] - prices[i]
                print(f"i am sub {prices[j]} with {prices[j]} so appending {max_price}")
                d.append(max_price)
                j +=1
            else:
                j +=1
            
        return max(d)
        
        