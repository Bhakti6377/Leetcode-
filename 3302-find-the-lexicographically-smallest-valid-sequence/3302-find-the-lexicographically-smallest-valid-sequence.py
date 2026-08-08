from bisect import bisect_left, bisect_right

class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # Store positions of every character in word1
        pos = [[] for _ in range(26)]

        for i, ch in enumerate(word1):
            pos[ord(ch) - ord('a')].append(i)

        # run_start[i] = start of the consecutive same-character run
        run_start = [0] * n
        for i in range(n):
            if i == 0 or word1[i] != word1[i - 1]:
                run_start[i] = i
            else:
                run_start[i] = run_start[i - 1]

        # run_end[i] = end of the consecutive same-character run
        run_end = [0] * n
        for i in range(n - 1, -1, -1):
            if i == n - 1 or word1[i] != word1[i + 1]:
                run_end[i] = i
            else:
                run_end[i] = run_end[i + 1]

        # exact[j]:
        # latest possible position of the first character of
        # word2[j:] when matching exactly.
        #
        # almost[j]:
        # latest possible position of the first character of
        # word2[j:] when at most one mismatch is allowed.
        exact = [-1] * (m + 1)
        almost = [-1] * (m + 1)

        # Empty suffix can start after the last index
        exact[m] = n
        almost[m] = n

        # Build suffix information from right to left
        for j in range(m - 1, -1, -1):
            c = ord(word2[j]) - ord('a')

            # Case 1: Match word2[j] exactly
            boundary = exact[j + 1]

            if boundary != -1:
                k = bisect_left(pos[c], boundary)

                if k > 0:
                    exact[j] = pos[c][k - 1]

                # Use the one allowed mismatch at this character
                if boundary > 0:
                    x = boundary - 1

                    if word1[x] != word2[j]:
                        almost[j] = x
                    else:
                        # Find the closest previous character
                        # that is different from word2[j]
                        x = run_start[x] - 1

                        if x >= 0:
                            almost[j] = x

            # Case 2: Match current character exactly,
            # and use the mismatch somewhere in the suffix
            boundary = almost[j + 1]

            if boundary != -1:
                k = bisect_left(pos[c], boundary)

                if k > 0:
                    almost[j] = max(
                        almost[j],
                        pos[c][k - 1]
                    )

        ans = []
        prev = -1
        used_mismatch = 0

        # Construct lexicographically smallest answer
        for j in range(m):
            c = ord(word2[j]) - ord('a')
            best = n
            next_used = used_mismatch

            # --------------------------------
            # Option 1: Match current character
            # --------------------------------
            k = bisect_right(pos[c], prev)

            if k < len(pos[c]):
                same = pos[c][k]

                if used_mismatch == 0:
                    # We can still use one mismatch later
                    if same < almost[j + 1]:
                        best = same
                        next_used = 0

                else:
                    # Mismatch already used,
                    # so the rest must match exactly
                    if same < exact[j + 1]:
                        best = same
                        next_used = 1

            # --------------------------------
            # Option 2: Use mismatch here
            # --------------------------------
            if used_mismatch == 0:
                x = prev + 1

                if x < n:
                    # Find first character after prev
                    # which is different from word2[j]
                    if word1[x] != word2[j]:
                        different = x
                    else:
                        different = run_end[x] + 1

                    # After using mismatch here,
                    # remaining suffix must match exactly
                    if different < n and different < exact[j + 1]:
                        if different < best:
                            best = different
                            next_used = 1

            # No valid position
            if best == n:
                return []

            ans.append(best)
            prev = best
            used_mismatch = next_used

        return ans