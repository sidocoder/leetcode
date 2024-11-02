class Solution:
    def divide(self, dividend, divisor):
        # Constants to handle 32-bit integer overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Special cases
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend == INT_MIN:
                return INT_MAX  # Handle overflow case
            else:
                return -dividend

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values to simplify calculations
        dividend, divisor = abs(dividend), abs(divisor)

        # Initialize quotient
        quotient = 0

        # Perform bitwise division
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        # Apply the correct sign to the quotient
        if negative:
            quotient = -quotient

        # Clamp the result to 32-bit signed integer range
        return min(max(INT_MIN, quotient), INT_MAX)
