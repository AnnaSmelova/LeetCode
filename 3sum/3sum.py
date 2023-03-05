class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            if i - 1 >= 0 and nums[i - 1] == nums[i]:
                continue
            while left < right:
                sum_current = nums[i] + nums[left] + nums[right]
                if sum_current == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif sum_current < 0:
                    left += 1
                else:
                    right -= 1
                    
        return result
                    
                    