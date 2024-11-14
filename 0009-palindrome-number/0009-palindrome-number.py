class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True

        return x == int(str(x)[::-1])

# Test the Solution class
sol = Solution()
input_numbers = [121, -121, 10]
for num in input_numbers:
    print(f"Input: {num}")
    print(f"Output: {sol.isPalindrome(num)}")