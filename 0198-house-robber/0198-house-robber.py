class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0
        for n in nums:
            first, second = second, max(second, first + n)
        return max(first, second)
        