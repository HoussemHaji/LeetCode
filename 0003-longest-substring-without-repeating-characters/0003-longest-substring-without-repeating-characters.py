class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        max_len = 0
        start = 0
        char_index_map = {}
        
        for end, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
            else:
                max_len = max(max_len, end - start + 1)
            char_index_map[char] = end
        
        return max_len
