class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 1

        if len(s) <= 1: return len(s)

        for i in range(len(s)):
            letters_sub = [s[i]]
            curr_sub = 1
            j = i + 1
            while (j < len(s)) and not (s[j] in letters_sub):
                letters_sub.append(s[j])
                curr_sub += 1
                j += 1
            
            if curr_sub > max_sub:
                max_sub = curr_sub

        return max_sub

"pwwkew"