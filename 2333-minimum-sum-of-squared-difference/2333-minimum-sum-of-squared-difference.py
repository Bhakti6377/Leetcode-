class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = sorted(
            (abs(a - b) for a, b in zip(nums1, nums2)),
            reverse=True
        )

        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.append(0)

        for i in range(len(nums1)):
            count = i + 1
            need = (diff[i] - diff[i + 1]) * count

            if k >= need:
                k -= need
            else:
                level = diff[i] - k // count
                remainder = k % count

                ans = remainder * (level - 1) ** 2
                ans += (count - remainder) * level ** 2

                ans += sum(x * x for x in diff[i + 1:-1])
                return ans

        return 0
