class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        max_reachable = 0
        jumps = 0
        current_max_reachable = 0
        for i in range(len(nums)):
            if i > current_max_reachable:
                jumps += 1
                current_max_reachable = max_reachable
            max_reachable = max(max_reachable, i + nums[i])
        return jumps
