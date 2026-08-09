class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # Suffix sum
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp(i, M) = maximum stones current player can get
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, M):
            if i >= n:
                return 0

            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            # Take X piles, where 1 <= X <= 2*M
            for X in range(1, 2 * M + 1):
                # Current player's stones =
                # all remaining stones - opponent's maximum
                opponent = dp(i + X, max(M, X))
                best = max(best, suffix[i] - opponent)

            return best

        return dp(0, 1)