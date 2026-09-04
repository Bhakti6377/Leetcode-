class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # suffix minimum
        min_right = [0] * n
        min_right[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            min_right[i] = min(nums[i], min_right[i + 1])

        # prefix maximum + check stability
        max_left = nums[0]

        for i in range(n):
            max_left = max(max_left, nums[i])

            if max_left - min_right[i] <= k:
                return i

        return -1