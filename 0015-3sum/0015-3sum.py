class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        
        res=[]
        
        
        nums.sort()
        
        for i,n in enumerate(nums):
            if  i>0 and nums[i-1] == nums[i]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                if (n+nums[l]+nums[r] == 0):
                    res.append([n,nums[l],nums[r]])
                        
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                        
                    l+=1
                    r-=1
                    
                elif (n+nums[l]+nums[r] < 0):
                    l+=1
                else:
                    r-=1
                    
        return res
            
                    
            