class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}
        return self.dp(N, K, memo)

    def dp(self, i, j, memo):
        if i == 0:
            return 0
        if j == 1:
            return i
        if (i, j) in memo:
            return memo[(i, j)]

        ans = sys.maxsize
        lo, hi = 1, i
        while lo <= hi:
            mid = (hi + lo) // 2
            broken = self.dp(mid - 1, j - 1, memo)
            not_broken = self.dp(i - mid, j, memo)
            if broken > not_broken:
                ans = min(ans, broken + 1)
                hi = mid - 1
            else:
                ans = min(ans, not_broken + 1)
                lo = mid + 1

        memo[(i, j)] = ans
        return ans
    
