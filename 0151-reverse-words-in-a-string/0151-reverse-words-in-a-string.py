class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        list = s.split(" ")
        result = ""
        for ele in list :
            if ele != "":
                result = ele + " " + result
            
        return result.strip()