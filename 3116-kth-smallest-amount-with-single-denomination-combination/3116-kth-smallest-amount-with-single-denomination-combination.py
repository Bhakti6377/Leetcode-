class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)

        # Remove redundant denominations.
        # If a coin is divisible by another coin, it doesn't create
        # any new amounts.
        coins.sort()

        filtered = []
        for c in coins:
            redundant = False

            for x in filtered:
                if c % x == 0:
                    redundant = True
                    break

            if not redundant:
                filtered.append(c)

        coins = filtered
        n = len(coins)

        # Count how many distinct amounts <= x can be formed
        def count(x):
            total = 0

            # Inclusion-exclusion over all subsets
            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1

                        # lcm(a,b) = a / gcd(a,b) * b
                        import math
                        g = math.gcd(lcm, coins[i])
                        lcm = lcm // g * coins[i]

                        if lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                amount = x // lcm

                if bits % 2 == 1:
                    total += amount
                else:
                    total -= amount

            return total

        # Binary search for the kth smallest amount
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left