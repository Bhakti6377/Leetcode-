class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0

        for num in nums:
            xor ^= num

        if xor != 0:
            return len(nums)

        # Total XOR is 0
        # Remove one non-zero element if possible
        for num in nums:
            if num != 0:
                return len(nums) - 1

        # All elements are zero
        return 0