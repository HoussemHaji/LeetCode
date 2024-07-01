class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        result = False
        i=0
        sum = 0
        while (sum<3) and (i<len(arr)):
            if arr[i]%2 != 0 :
                sum+=1
                
            else :
                sum = 0
               
                    
            i+=1
            
            if sum == 3 :
                result = True
                break
                
        return result
            
        