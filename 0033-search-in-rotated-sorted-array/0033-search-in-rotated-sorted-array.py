from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:  # Use <= to include both ends in the search
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            # Check if left half is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:  # target in left sorted part
                    r = m - 1
                else:
                    l = m + 1
            # Right half must be sorted
            else:
                if nums[m] < target <= nums[r]:  # target in right sorted part
                    l = m + 1
                else:
                    r = m - 1
        
        return -1  # Return -1 if the target is not found
