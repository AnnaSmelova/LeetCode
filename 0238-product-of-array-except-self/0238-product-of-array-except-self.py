class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]
        tmp = 1
        for j in range(n - 2, -1, -1):
            nums[j], tmp = nums[j + 1] * tmp, nums[j]
            answer[j] *= nums[j]
        return answer
            
        