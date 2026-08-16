class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        # Stones divisible by 3
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0

        # Odd number of 0-mod-3 stones
        return abs(cnt[1] - cnt[2]) > 2