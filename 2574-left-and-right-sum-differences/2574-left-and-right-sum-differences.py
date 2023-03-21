class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n
        for i in range(1, n):
            j = n - i - 1
            left_sum[i] = left_sum[i - 1] + nums[i - 1]
            right_sum[i] = right_sum[i - 1] + nums[j + 1]
        for i in range(n):
            left_sum[i] -= right_sum[n - i - 1]
            if left_sum[i] < 0:
                left_sum[i] *= -1
        return left_sum
