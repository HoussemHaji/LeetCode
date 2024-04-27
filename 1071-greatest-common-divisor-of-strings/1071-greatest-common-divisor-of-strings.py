class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) > len(str2):
            small = str2
        if len(str1) <= len(str2):
            small = str1
        gcd = 1
        for i in range(1,len(small) + 1):
            if (len(str1) % i == 0) and (len(str2) % i == 0):
                gcd = i
        return str1[:gcd]
                