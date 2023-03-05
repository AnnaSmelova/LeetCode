class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stack = []
        for n in nums:
            if stack and n <= stack[-1]:
                left, right = 0, len(stack)
                while left < right:
                    mid = (left + right) // 2
                    if stack[mid] < n:
                        left = mid + 1
                    else:
                        right = mid
                stack[right] = n
            else:
                stack.append(n)
                if len(stack) == 3:
                    return True
        return False
        