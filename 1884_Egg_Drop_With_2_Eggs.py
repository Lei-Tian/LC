#!/usr/bin/env python
# coding=utf-8
class Solution:
    def twoEggDrop(self, n: int) -> int:
        return self.helper(n, 2, {})
    
    def helper(self,n, k, memo):
        if k == 1:
            return n
        if n == 0:
            return 0
        if (n, k) in memo:
            return memo[(n, k)]
        
        ans = sys.maxsize
        lo, hi = 1, n
        while lo <= hi:
            mid = (hi + lo) // 2
            broken = self.helper(mid - 1, k - 1, memo)
            not_broken = self.helper(n - mid, k, memo)
            if broken > not_broken:
                hi = mid - 1
                ans = min(ans, broken + 1)
            else:
                lo = mid + 1
                ans = min(ans, not_broken + 1)
        
        memo[(n, k)] = ans
        return ans
