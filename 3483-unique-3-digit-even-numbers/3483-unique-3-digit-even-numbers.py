class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = 0

        for num in range(100, 1000):
            if num % 2 != 0:
                continue

            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            required = [a, b, c]

            if all(required.count(d) <= digits.count(d) for d in set(required)):
                count += 1

        return count