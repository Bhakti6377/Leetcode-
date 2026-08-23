class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0

        left_q = 0
        right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # Difference in number of '?' must be even
        if (left_q - right_q) % 2 != 0:
            return True

        # Difference in '?' contributes 9 points per pair
        return left_sum - right_sum != (right_q - left_q) * 9 // 2