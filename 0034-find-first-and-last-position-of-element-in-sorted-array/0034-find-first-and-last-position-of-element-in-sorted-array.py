class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        target_pos = [-1, -1]
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                i, j = mid, mid
                while i >= 0 and nums[i] == target:
                    i -= 1
                target_pos[0] = i + 1
                while j < len(nums) and nums[j] == target:
                    j += 1
                target_pos[1] = j - 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return target_pos

        