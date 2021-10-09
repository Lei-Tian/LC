#!/usr/bin/env python
# coding=utf-8
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n < 3:
            return k ** n
        dp0, dp1, dp2 = k, k * k, 0
        for i in range(2, n):
            dp2 = (k - 1) * (dp0 + dp1)
            dp0 = dp1
            dp1 = dp2
        return dp2
