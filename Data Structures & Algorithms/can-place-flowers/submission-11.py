class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = n
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 1 and n >1:
            return False
        for i in range(len(flowerbed)):
            if i == 0:
                if not flowerbed[i] and not flowerbed[i+1]:
                    flowerbed[i] = 1
                    k -=1
            elif i == len(flowerbed) -1:
                if not flowerbed[i -1] and not flowerbed[i]: 
                    flowerbed[i] = 1
                    k -=1
            elif not flowerbed[i -1] and not flowerbed[i+1] and not flowerbed[i]:
                print("at i", i, " prev is ",flowerbed[i -1], "next is ",flowerbed[i+1], "current is", flowerbed[i])
                flowerbed[i] = 1
                k -=1
            
        return k <= 0