class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, num in enumerate(nums):
            if target - num in s.keys():
               return [i, s[target - num]]
            else:
                s[num] = i
        