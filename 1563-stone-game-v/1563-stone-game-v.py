from functools import cache

class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)

        # Prefix sums
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @cache
        def dfs(i, j):
            if i == j:
                return 0

            ans = 0
            left = 0
            right = prefix[j + 1] - prefix[i]

            for k in range(i, j):
                left += stoneValue[k]
                right -= stoneValue[k]

                # Left side is smaller
                if left < right:

                    # Pruning:
                    # If current answer is already >= 2 * left,
                    # this split cannot improve the answer.
                    if ans >= 2 * left:
                        continue

                    ans = max(
                        ans,
                        left + dfs(i, k)
                    )

                # Right side is smaller
                elif left > right:

                    # Since right keeps decreasing,
                    # later splits cannot improve the answer.
                    if ans >= 2 * right:
                        break

                    ans = max(
                        ans,
                        right + dfs(k + 1, j)
                    )

                # Equal
                else:
                    ans = max(
                        ans,
                        left + dfs(i, k),
                        right + dfs(k + 1, j)
                    )

            return ans

        return dfs(0, n - 1)