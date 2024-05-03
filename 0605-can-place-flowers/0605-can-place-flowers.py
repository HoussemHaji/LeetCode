class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if 1 not in flowerbed:
            return (n - ((len(flowerbed) + 1) //2))<= 0
        
        if flowerbed[0] == 0:      
            
            n = n - flowerbed.index(1)//2
        start = 0
        end = flowerbed.index(1)
            
        
        while (1 in flowerbed) and (flowerbed.index(1) != (len(flowerbed)-1)) :
            
            start = flowerbed.index(1)
            
            flowerbed[flowerbed.index(1)]= 0
            if 1 in flowerbed :
                end = flowerbed.index(1)
                n = n - (end - start - 2)//2
            else : 
                end = len(flowerbed) - 1
                n = n - (end - start )//2
            
        return (n <= 0)