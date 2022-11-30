class Solution:
    def isPalindrome(self, x: int) -> bool:
        char_int = str(x)
        start = 0
        size = len(char_int)

        while start < size - start - 1:
            if char_int[start] != char_int[size - start - 1]:
                return False

            start += 1
        
        return True