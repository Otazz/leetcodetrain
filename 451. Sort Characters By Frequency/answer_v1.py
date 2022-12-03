from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        freq_by_letter = defaultdict(int)
        max_freq = 0

        for c in s:
            freq_by_letter[c] += 1
            if freq_by_letter[c] > max_freq:
                max_freq = freq_by_letter[c]
        
        freqs = [""] * max_freq

        for c in freq_by_letter:
            freqs[freq_by_letter[c] - 1] += c*freq_by_letter[c]

        return "".join(reversed(freqs))
