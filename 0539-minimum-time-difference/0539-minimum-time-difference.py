class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        for i,e in enumerate(timePoints) :
            timePoints[i] = int(e.split(":")[0])*60 + int(e.split(":")[1])
            
            
        timePoints.sort()
        
        currMin = float('inf')
        
        for i in range(1, len(timePoints)):
            currMin = min(currMin, timePoints[i] - timePoints[i-1])
            
        
        currMin = min(currMin, (60*24) - timePoints[-1] + timePoints[0])
        
        return currMin
        
        