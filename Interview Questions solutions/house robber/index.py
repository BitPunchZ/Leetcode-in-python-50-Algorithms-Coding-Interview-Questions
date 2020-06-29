class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n==0):
            return 0
        
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1,n):
            if(i==1):
                dp[i] = max(nums[0],nums[1])
            else:
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
        return dp[-1]

        