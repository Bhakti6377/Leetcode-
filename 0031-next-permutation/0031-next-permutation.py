class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i = i - 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j = j - 1
            nums[i], nums[j] = nums[j], nums[i]

        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left = left + 1
            right = right - 1
        
        