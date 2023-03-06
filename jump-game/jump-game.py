class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        dp = [0] * n
        dp[0] = 1
        for i, num in enumerate(nums):
            if dp[i]:
                for j in range(1, num + 1):
                    k = i + j
                    if k == n - 1:
                        return True
                    if k < n:
                        dp[k] = 1
        return False
    