class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)

        # If k == 1, each element itself is a subarray
        if k == 1:
            count = {}

            for x in nums:
                count[x] = count.get(x, 0) + 1

            ans = -1

            for x in nums:
                if count[x] == 1:
                    ans = max(ans, x)

            return ans

        # If k == n, there is only one subarray: the whole array
        if k == n:
            return max(nums)

        # For 1 < k < n, only first and last elements
        # can appear in exactly one size-k subarray.

        first = nums[0]
        last = nums[n - 1]

        # Check if first element appears anywhere else
        first_ok = True
        for i in range(1, n):
            if nums[i] == first:
                first_ok = False
                break

        # Check if last element appears anywhere else
        last_ok = True
        for i in range(n - 1):
            if nums[i] == last:
                last_ok = False
                break

        ans = -1

        if first_ok:
            ans = max(ans, first)

        if last_ok:
            ans = max(ans, last)

        return ans