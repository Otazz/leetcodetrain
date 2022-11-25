from math import sqrt, floor
class Solution:
    def numSquares(self, n: int) -> int:
        memory = {1: 1, 0:0}
        squares_memory = {}

        def dpSquares(n):
            for i in range(1, n+1):
                min_count = n
                nearest_square = floor(sqrt(i)) + 1
                for j in range(1, nearest_square):
                    if j not in squares_memory:
                        squares_memory[j] = j*j
                    count = 1 + memory[i - squares_memory[j]]
                    if count < min_count:
                        min_count = count
                memory[i] = min_count
            return memory[n]
        
        return dpSquares(n)

print(Solution().numSquares(12))
