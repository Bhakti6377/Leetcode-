class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        total = 10
        unique = 9
        available = 9

        while n > 1 and available > 0:
            unique = unique * available
            total = total + unique

            available = available - 1
            n = n - 1

        return total