class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        mydict = {}
        
        for n in nums :
            if n not in mydict.keys():
                mydict[n]=1
            else: mydict[n]+=1
        
        sorted_elements = sorted(mydict,key=mydict.get,reverse=True)
        
        return sorted_elements[:k]
        
        