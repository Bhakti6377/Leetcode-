class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Step 1: Find first and last occurrence of each character
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Step 2: Generate valid minimum-length intervals
        for c in range(26):
            if last[c] == -1:
                continue

            left = first[c]
            right = last[c]
            i = left
            valid = True

            while i <= right:
                x = ord(s[i]) - ord('a')

                # Character appears before this interval
                if first[x] < left:
                    valid = False
                    break

                # Expand interval to include all occurrences
                right = max(right, last[x])
                i += 1

            if valid:
                intervals.append((left, right))

        # Step 3: Greedy selection by earliest ending position
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right

        return result