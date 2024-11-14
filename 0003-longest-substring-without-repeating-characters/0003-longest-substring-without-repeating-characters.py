class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_index_map = {}
        max_length = 0
        start = 0

        for i, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
            char_index_map[char] = i
            max_length = max(max_length, i - start + 1)

        return max_length

# Test the Solution class
sol = Solution()
input_strings = ["abcabcbb", "bbbbb", "pwwkew"]
for s in input_strings:
    print(f"Input: {s}")
    print(f"Output: {sol.lengthOfLongestSubstring(s)}")