class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        prefix =[1]*len(nums)
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]* nums[i-1]
            
        suffix = [1]*len(nums)
        
        for i in range(len(nums)-2,-1,-1):
            suffix[i]= suffix[i+1]* nums[i+1]
         
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i]*suffix[i]
            
        return res
            
            
        