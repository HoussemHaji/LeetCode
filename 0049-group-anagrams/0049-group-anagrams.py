class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        res = {}
        
        for s in strs :
            count = [0] * 26
            
            for c in s :
                count[ord(c) - ord('a')] +=1
                
            if(tuple(count) not in res.keys()):
                res[tuple(count)] = [s]
            else: res[tuple(count)].append(s)
                
        return res.values()