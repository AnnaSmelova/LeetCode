class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        result = 1
        for i in nums:
            if i > 0 and i == result:
                result += 1
            elif i > result:
                return result
        return result
