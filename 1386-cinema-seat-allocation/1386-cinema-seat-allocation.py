class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Store reserved seats only for rows that actually have reservations
        rows = {}

        for r, s in reservedSeats:
            if r not in rows:
                rows[r] = set()
            rows[r].add(s)

        # Initially, every row can have 2 groups
        # Rows without reservations contribute 2 groups each
        ans = (n - len(rows)) * 2

        # Check only rows with reserved seats
        for seats in rows.values():

            # Possible blocks:
            # Left  -> 2,3,4,5
            # Middle -> 4,5,6,7
            # Right -> 6,7,8,9

            left = all(s not in seats for s in [2, 3, 4, 5])
            right = all(s not in seats for s in [6, 7, 8, 9])

            if left and right:
                # Both sides can be used
                ans += 2

            elif left or right:
                # One side can be used
                ans += 1

            elif all(s not in seats for s in [4, 5, 6, 7]):
                # Only middle block can be used
                ans += 1

        return ans