class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "AEIOU"
        vowels_target=""
        for ele in s :
            if ele.upper() in vowels:
                 vowels_target =  ele + vowels_target
                 
        result = s
        for i,ele in enumerate(s):
            if ele.upper() in vowels:
                result = result[:i] + vowels_target[0] + result[i+1:]
                vowels_target = vowels_target[1:]
               
                
        return result