from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        freq_by_letter = defaultdict(int)

        for c in s:
            freq_by_letter[c] += 1
        
        freqs = [k*v for k, v in sorted(freq_by_letter.items(), key=lambda x: x[1], reverse=True)]

        return "".join(freqs)
