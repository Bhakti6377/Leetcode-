class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If there is only one row, no conversion is needed
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        current_row = 0
        direction = 1  # 1 = down, -1 = up

        for ch in s:
            rows[current_row] += ch

            # Change direction at the top or bottom
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        return "".join(rows)
