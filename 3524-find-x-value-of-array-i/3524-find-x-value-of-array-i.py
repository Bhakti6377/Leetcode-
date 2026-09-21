from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp = [0] * k
        result = [0] * k

        for num in nums:
            num %= k

            new_dp = [0] * k

            # Subarrays starting at the current element
            new_dp[num] += 1

            # Extend previous subarrays
            for r in range(k):
                new_dp[(r * num) % k] += dp[r]

            dp = new_dp

            # Count all subarrays ending here
            for r in range(k):
                result[r] += dp[r]

        return result