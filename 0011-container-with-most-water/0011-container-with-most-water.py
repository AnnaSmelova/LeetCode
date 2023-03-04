class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            left_height = height[i]
            right_height = height[j]
            area = (j - i) * min(left_height, right_height)
            max_area = max(max_area, area)
            if left_height > right_height:
                while i < j and right_height > height[j - 1]:
                    j -= 1
                if i < j:
                    j -= 1
            else:
                while i < j and left_height > height[i + 1]:
                    i += 1
                if i < j:
                    i += 1
        return max_area
                
            