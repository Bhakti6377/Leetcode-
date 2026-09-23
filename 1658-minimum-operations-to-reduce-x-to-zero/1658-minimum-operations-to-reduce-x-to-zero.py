class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:

        total = sum(nums)
        target = total - x

        # If target is negative, impossible
        if target < 0:
            return -1

        left = 0
        current_sum = 0
        max_len = -1

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > target:
                current_sum -= nums[left]
                left += 1

            if current_sum == target:
                max_len = max(max_len, right - left + 1)

        # Remove everything except the longest valid subarray
        if max_len == -1:
            return -1

        return len(nums) - max_len     