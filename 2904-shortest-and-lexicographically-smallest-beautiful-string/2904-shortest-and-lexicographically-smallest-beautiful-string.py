class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            if ones == k:
                # Remove leading zeros to make the substring shortest
                while s[left] == '0':
                    left += 1

                current = s[left:right + 1]

                # Update answer
                if not ans or len(current) < len(ans):
                    ans = current
                elif len(current) == len(ans) and current < ans:
                    ans = current

                # Move past the first 1
                ones -= 1
                left += 1

        return ans