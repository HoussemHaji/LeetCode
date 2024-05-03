class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        
        if ch not in word :
            return word
        
        idx = word.index(ch)
        
        result= ""
        
        for i in range(idx + 1):
            result = word[0] + result
            word = word[1:]
            
        return result + word
            
            
            
            
        