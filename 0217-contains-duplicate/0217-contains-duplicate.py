class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        hashset = set()
        
        for e in nums:
            if e in hashset : 
                return True
            
            hashset.add(e)
        
        return False
            
            