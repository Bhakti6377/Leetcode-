class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        h = {}

        for i in range(len(nums)):
            if nums[i] in h:
                if i - h[nums[i]] <= k:
                    return True

            h[nums[i]] = i

        return False
        