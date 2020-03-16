class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        n = len(nums)

        for i in range(0,n):
            val = target-nums[i]
            if(val in m):
                return [m[target-num[i]], i]
            m[nums[i]] = i