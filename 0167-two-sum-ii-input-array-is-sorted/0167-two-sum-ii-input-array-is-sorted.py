class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n
        while i < j:
            mid = (i + j) // 2
            if target - numbers[mid] == numbers[i]:
                return [i + 1, mid + 1]
            elif target - numbers[mid] == numbers[j - 1]:
                return [mid + 1, j]
            elif target - numbers[mid] < numbers[i]:
                j = mid
            elif target - numbers[mid] > numbers[j - 1]:
                i = mid + 1
            else:
                if target > numbers[i] + numbers[j - 1]:
                    i += 1
                elif target < numbers[j - 1] + numbers[i]:
                    j -= 1
                else:
                    return [i + 1, j]
            
