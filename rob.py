#198. House Robber
def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0]*n
        for i in range(n):
            dp[i] = max(0 if i==0 else nums[i-1],nums[i]+ (max(dp[0:i-1]) if i>1 else 0))
        return max(dp)
