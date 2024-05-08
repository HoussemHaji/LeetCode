class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_amount = 0
        while i<j :
            if (j-i)*min(height[i], height[j]) > max_amount :
                max_amount = (j-i)*min(height[i], height[j])
            
            if height[j]> height[i]:
                i += 1
            else: j-=1
                    
        return max_amount