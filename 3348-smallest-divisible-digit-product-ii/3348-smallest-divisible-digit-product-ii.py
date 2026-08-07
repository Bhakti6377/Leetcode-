class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Factorize t into prime factors 2, 3, 5, 7
        temp = t
        counts = {2: 0, 3: 0, 5: 0, 7: 0}

        for p in [2, 3, 5, 7]:
            while temp % p == 0:
                counts[p] += 1
                temp //= p

        # If t has prime factors other than 2, 3, 5, 7, impossible
        if temp > 1:
            return "-1"

        # Helper to compute minimum digits required
        def min_length_needed(c2, c3, c5, c7):
            c2 = max(0, c2)
            c3 = max(0, c3)
            c5 = max(0, c5)
            c7 = max(0, c7)

            d9 = c3 // 2
            r3 = c3 % 2

            d8 = c2 // 3
            r2 = c2 % 3

            d7 = c7
            d5 = c5

            d6 = 0
            if r2 == 1 and r3 == 1:
                d6 = 1
                r2, r3 = 0, 0
            elif r2 == 2 and r3 == 1:
                d6 = 1
                r2, r3 = 1, 0

            d4 = r2 // 2
            r2 %= 2

            d3 = r3
            d2 = r2

            return d9 + d8 + d7 + d6 + d5 + d4 + d3 + d2

        def get_suffix(rem_len, c2, c3, c5, c7):
            res = []

            for _ in range(rem_len):
                for d in range(1, 10):
                    nc2 = c2 - (
                        1 if d in (2, 6)
                        else 2 if d == 4
                        else 3 if d == 8
                        else 0
                    )

                    nc3 = c3 - (
                        1 if d in (3, 6)
                        else 2 if d == 9
                        else 0
                    )

                    nc5 = c5 - (1 if d == 5 else 0)
                    nc7 = c7 - (1 if d == 7 else 0)

                    if min_length_needed(nc2, nc3, nc5, nc7) <= rem_len - len(res) - 1:
                        res.append(str(d))
                        c2, c3, c5, c7 = nc2, nc3, nc5, nc7
                        break

            return "".join(res)

        n = len(num)

        first_zero = num.find("0")
        limit = first_zero if first_zero != -1 else n

        pref_c2 = [0] * (n + 1)
        pref_c3 = [0] * (n + 1)
        pref_c5 = [0] * (n + 1)
        pref_c7 = [0] * (n + 1)

        for i in range(limit):
            d = int(num[i])

            pref_c2[i + 1] = pref_c2[i] + (
                1 if d in (2, 6)
                else 2 if d == 4
                else 3 if d == 8
                else 0
            )

            pref_c3[i + 1] = pref_c3[i] + (
                1 if d in (3, 6)
                else 2 if d == 9
                else 0
            )

            pref_c5[i + 1] = pref_c5[i] + (1 if d == 5 else 0)
            pref_c7[i + 1] = pref_c7[i] + (1 if d == 7 else 0)

        if first_zero == -1:
            req2 = counts[2] - pref_c2[n]
            req3 = counts[3] - pref_c3[n]
            req5 = counts[5] - pref_c5[n]
            req7 = counts[7] - pref_c7[n]

            if req2 <= 0 and req3 <= 0 and req5 <= 0 and req7 <= 0:
                return num

        for i in range(limit, -1, -1):
            start_digit = int(num[i]) + 1 if i < n else 1

            for d in range(start_digit, 10):
                c2 = counts[2] - pref_c2[i] - (
                    1 if d in (2, 6)
                    else 2 if d == 4
                    else 3 if d == 8
                    else 0
                )

                c3 = counts[3] - pref_c3[i] - (
                    1 if d in (3, 6)
                    else 2 if d == 9
                    else 0
                )

                c5 = counts[5] - pref_c5[i] - (1 if d == 5 else 0)
                c7 = counts[7] - pref_c7[i] - (1 if d == 7 else 0)

                rem_len = n - 1 - i

                if min_length_needed(c2, c3, c5, c7) <= rem_len:
                    prefix = num[:i] + str(d)
                    suffix = get_suffix(rem_len, c2, c3, c5, c7)
                    return prefix + suffix

        total_len = max(
            n + 1,
            min_length_needed(
                counts[2],
                counts[3],
                counts[5],
                counts[7],
            ),
        )

        return get_suffix(
            total_len,
            counts[2],
            counts[3],
            counts[5],
            counts[7],
        )