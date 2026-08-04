class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = []

        smallest = min(nums)
        largest = max(nums)

        num_set = set(nums)

        for i in range(smallest, largest + 1):
            if i not in num_set:
                result.append(i)

        return result