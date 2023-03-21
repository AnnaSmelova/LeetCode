class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        temp = 0
        for n in nums:
            if n == 0:
                temp += 1
            else:
                temp = 0
            result += temp
        return result
        