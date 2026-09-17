
from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = n + 1

        best = [INF] * n
        left = 0
        curr_sum = 0
        min_len = INF
        ans = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # Combine with the best subarray
                # ending before this one starts.
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, best[left - 1] + length)

                min_len = min(min_len, length)

            # Best subarray found so far
            best[right] = min(
                min_len,
                best[right - 1] if right > 0 else INF
            )

        return ans if ans != INF else -1