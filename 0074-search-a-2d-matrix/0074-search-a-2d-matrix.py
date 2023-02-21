class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        arr = []
        if m == 1:
            arr = matrix[0]
        for i in range(1, m):
            if target < matrix[i][0]:
                arr = matrix[i - 1]
                break
        if not arr:
            arr = matrix[-1]
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return False
    