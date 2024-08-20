class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        nums.sort()
        
        res = False
        
        if(len(nums)<=1):
            return False
        
        i=0
        
        while(i<len(nums)-1):
            left = nums[i]
            right = nums[i+1]
            if left == right :
                return True
            
            i = i+1

            
        return False
            
            