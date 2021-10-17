class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        dp = [{} for i in range(n)]
        for i in range(n):
            for j in range(i):
                delta = nums[i] - nums[j]
                dp[i][delta] = dp[i].get(delta, 0) + dp[j].get(delta, 0) + 1
                ans += dp[j].get(delta, 0)
        return ans
