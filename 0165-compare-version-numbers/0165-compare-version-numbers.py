class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        if ("." not in version1) and ("." not in version2):
            if int(version1) < int(version2) :
                return -1
            elif int(version2) < int(version1):
                return 1
            else :
                return 0
            
        versionList1 = version1.split(".")
        versionList2 = version2.split(".")
        
        
        while versionList2 and versionList1:
            if int(versionList1[0]) < int(versionList2[0]) :
                return -1
            elif int(versionList2[0]) < int(versionList1[0]):
                return 1
            else :
                versionList1.pop(0)
                versionList2.pop(0)
                
        if len(versionList1) != 0:
            if any(int(item) != 0 for item in versionList1):
                return 1
            else: 
                return 0
        if len(versionList2) != 0:
            if any(int(item) != 0 for item in versionList2):
                return -1
            else: 
                return 0
            
        return 0
            
            
            
            
                
            
        
            
        
                 