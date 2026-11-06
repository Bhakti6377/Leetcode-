class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])

        q = sorted((t, i) for i, t in enumerate(queries))

        count = {}
        ans = [0] * len(queries)

        left = right = 0

        for t, idx in q:
            start = t - x

            while right < len(logs) and logs[right][1] <= t:
                s = logs[right][0]
                count[s] = count.get(s, 0) + 1
                right += 1

            while left < right and logs[left][1] < start:
                s = logs[left][0]
                count[s] -= 1

                if count[s] == 0:
                    del count[s]

                left += 1

            ans[idx] = n - len(count)

        return ans