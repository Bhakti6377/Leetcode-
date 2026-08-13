class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:

        n = len(s)

        # Each node stores:
        # [left_char, right_char, prefix, suffix, best, length]
        tree = [None] * (4 * n)

        def merge(a, b):
            left_char = a[0]
            right_char = b[1]

            prefix = a[2]
            suffix = b[3]

            best = max(a[4], b[4])

            # If both boundary characters are same,
            # we can join suffix of left + prefix of right
            if a[1] == b[0]:
                best = max(best, a[3] + b[2])

                # Entire left segment has same character
                if a[2] == a[5]:
                    prefix = a[5] + b[2]

                # Entire right segment has same character
                if b[3] == b[5]:
                    suffix = b[5] + a[3]

            length = a[5] + b[5]

            return [
                left_char,
                right_char,
                prefix,
                suffix,
                best,
                length
            ]

        def build(node, l, r):
            if l == r:
                tree[node] = [
                    s[l],   # left_char
                    s[l],   # right_char
                    1,      # prefix
                    1,      # suffix
                    1,      # best
                    1       # length
                ]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, char):
            if l == r:
                tree[node] = [
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                ]
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        # Build initial tree
        build(1, 0, n - 1)

        ans = []

        # Process every query
        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)

            # Root contains answer for entire string
            ans.append(tree[1][4])

        return ans