class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        dp = prefix[n]

        for i in range(n - 1, 1, -1):
            dp = max(dp, prefix[i] - dp)

        return dp