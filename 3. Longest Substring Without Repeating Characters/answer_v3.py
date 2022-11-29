class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0

        start_sub = 0

        letters_sub = {}

        for i, ch in enumerate(s):
            if ch in letters_sub:
                start_sub = max(letters_sub[ch] + 1, start_sub)

            letters_sub[ch] = i
            max_sub = max(i - start_sub + 1, max_sub)

        return max_sub