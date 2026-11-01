class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mini = min(nums)
        return sum(nums) - len(nums) * mini