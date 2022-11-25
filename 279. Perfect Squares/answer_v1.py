from math import sqrt, floor
class Solution:
    def numSquares(self, n: int) -> int:
        memory = {1: 1, 0:0}
        squares_memory = {}
        nearest_square = floor(sqrt(n)) + 1

        def bfsSquares(crr_n, memory):
            if crr_n in memory:
                return memory[crr_n]

            min_count = n
            for i in range(1, nearest_square):
                if i not in squares_memory:
                    squares_memory[i] = i*i
                if crr_n - squares_memory[i] >= 0:
                    count = 1 + bfsSquares(crr_n - squares_memory[i], memory)
                    if count < min_count:
                        min_count = count
            memory[crr_n] = min_count
        
            return min_count

        
        return bfsSquares(n, memory)

print(Solution().numSquares(6337))

# def bfsSquares(crr_n):
#     if crr_n in memory:
#         print(crr_n)
#         return memory[crr_n]
#     result = []
#     for i in range(1, floor(sqrt(crr_n)) + 1):
#         if i not in squares_memory:
#             squares_memory[i] = i*i
#         if crr_n - squares_memory[i] >= 0:
#             res = [squares_memory[i]] + bfsSquares(crr_n - squares_memory[i])
#             if not result:
#                 result = res
#             if len(result) > len(res):
#                 result = res
#     if crr_n not in memory or len(memory[crr_n]) > len(result):
#         memory[crr_n] = result
#     print(memory)
#     return result