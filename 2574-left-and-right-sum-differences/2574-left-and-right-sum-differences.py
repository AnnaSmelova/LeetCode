class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n
        for i in range(1, n):
            j = n - i - 1
            left_sum[i] = left_sum[i - 1] + nums[i - 1]
            right_sum[i] = right_sum[i - 1] + nums[j + 1]
        right_sum = right_sum[::-1]
        answer = [0] * n
        for i in range(n):
            answer[i] = left_sum[i] - right_sum[i]
            if answer[i] < 0:
                answer[i] *= -1
        return answer
