class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = 1
        for i in range(len(nums)):
            dp = max(dp - 1, nums[i]) if dp > 0 else -1
        
        return dp >= 0
    