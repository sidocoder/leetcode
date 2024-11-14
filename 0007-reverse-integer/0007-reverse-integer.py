class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1

        reversed_x = 0
        while x != 0:
            pop = x % 10
            x = x // 10

            # Check for overflow
            if reversed_x > (2**31 - 1) // 10 or (reversed_x == (2**31 - 1) // 10 and pop > 7):
                return 0

            reversed_x = reversed_x * 10 + pop

        return sign * reversed_x
        