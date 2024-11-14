class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        zigzag = [''] * numRows
        row, step = 0, 1

        for char in s:
            zigzag[row] += char
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step

        return ''.join(zigzag)

# Test the Solution class
sol = Solution()
inputs = [("PAYPALISHIRING", 3), ("PAYPALISHIRING", 4), ("A", 1)]
for s, numRows in inputs:
    print(f"Input: '{s}', numRows: {numRows}")
    print(f"Output: '{sol.convert(s, numRows)}'")