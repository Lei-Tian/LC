#!/usr/bin/env python
# coding=utf-8
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[[sys.maxsize for k in range(n)] for j in range(target + 1)] for i in range(m + 1)]
        for k in range(n):
            dp[0][0][k] = 0
        
        for i in range(1, m + 1):
            if houses[i - 1] == 0:
                for j in range(1, target + 1):
                    firstIndex, secondIndex = self.find_first_second(dp[i - 1][j - 1])
                    for k in range(n):
                        if k != firstIndex:
                            dp[i][j][k] = min(dp[i - 1][j - 1][firstIndex], dp[i - 1][j][k]) + cost[i - 1][k]
                        else:
                            dp[i][j][k] = min(dp[i - 1][j - 1][secondIndex], dp[i - 1][j][k]) + cost[i - 1][k]
            else:
                for j in range(1, target + 1):
                    k = houses[i - 1] - 1
                    for l in range(n):
                        if l == k:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][l])
                        else:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - 1][l])
        ans = sys.maxsize
        for k in range(n):
            ans = min(ans, dp[m][target][k])
        if ans == sys.maxsize:
            return -1
        return ans
    
    def find_first_second(self, nums):
        firstIndex, secondIndex = None, None
        for index, num in enumerate(nums):
            if firstIndex is None or nums[firstIndex] >= num:
                secondIndex = firstIndex
                firstIndex = index
            elif secondIndex is None or nums[secondIndex] > num:
                secondIndex = index
        return firstIndex, secondIndex
