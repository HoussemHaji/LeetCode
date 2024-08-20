class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s)!= len(t):
            return False
        
        dict = {}
        
        for c in s :
            if not(c in dict.keys()) :
                dict[c] = 1
            else :
                dict[c] += 1
                
        for c in t:
            if c not in dict.keys():
                return False
            if dict[c] == 0 :
                return False
            
            dict[c] -= 1
            
        return True