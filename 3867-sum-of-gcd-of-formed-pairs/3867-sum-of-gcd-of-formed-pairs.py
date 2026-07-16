from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        mx = 0

        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(gcd(num, mx))

        prefixGcd.sort()

        ans = 0
        i = 0
        j = len(prefixGcd) - 1

        while i < j:
            ans = ans + gcd(prefixGcd[i], prefixGcd[j])
            i = i + 1
            j = j - 1

        return ans