class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        ans = []

        for i in range(len(target)):
            t = ord(target[i]) - ord('a')

            if freq[t] > 0:
                ans.append(target[i])
                freq[t] -= 1
                continue

            for c in range(t + 1, 26):
                if freq[c] > 0:
                    ans.append(chr(c + ord('a')))
                    freq[c] -= 1

                    for x in range(26):
                        ans.extend(chr(x + ord('a')) * freq[x])

                    return ''.join(ans)

            break

        while ans:
            prev = ans.pop()
            p = ord(prev) - ord('a')
            freq[p] += 1

            for c in range(p + 1, 26):
                if freq[c] > 0:
                    ans.append(chr(c + ord('a')))
                    freq[c] -= 1

                    for x in range(26):
                        ans.extend(chr(x + ord('a')) * freq[x])

                    return ''.join(ans)

        return ""