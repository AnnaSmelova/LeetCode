class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range((n - 1)//2 + 1):
            result += [nums[2 * i + 1]] * nums[2 * i]
        return result
