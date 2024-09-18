class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert all numbers to strings for easier comparison
        nums = list(map(str, nums))

        # Sort using a custom comparator by comparing concatenated strings
        nums.sort(key=lambda x: x * 10, reverse=True)  # Multiply to simulate lexicographical comparison
        
        # Join the sorted array into a single string
        res = ''.join(nums)
        
        # Edge case: if the largest number is '0', return '0'
        if res[0] == '0':
            return '0'
        
        return res

                    
                    
                    

                
        