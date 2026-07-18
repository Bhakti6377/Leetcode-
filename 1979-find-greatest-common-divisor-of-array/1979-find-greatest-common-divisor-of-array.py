class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        large = max(nums)

        while large % small != 0:
            large, small = small, large % small

        return small