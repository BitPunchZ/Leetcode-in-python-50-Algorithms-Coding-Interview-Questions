class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 0):
            return 0

        dp = [0] * n
        dp[0] = nums[0]

        for i in range(n):
            dp[i] = nums[0] if i == 0 else (
                max(nums[0], nums[1]) if i == 1
                else max(dp[i-1], dp[i-2]+nums[i])
            )
        return dp[n-1]
