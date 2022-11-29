class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = curr_sub = 0

        if len(s) <= 1: return len(s)

        start_sub = 0

        letters_sub = {}

        for i in range(len(s)):
            if s[i] in letters_sub and letters_sub[s[i]] >= start_sub:
                if curr_sub > max_sub:
                    max_sub = curr_sub
                    
                curr_sub = curr_sub + start_sub - letters_sub[s[i]]
                start_sub = letters_sub[s[i]] + 1
                letters_sub[s[i]] = i
            else:
                letters_sub[s[i]] = i
                curr_sub += 1
            
        if curr_sub > max_sub:
            max_sub = curr_sub

        return max_sub