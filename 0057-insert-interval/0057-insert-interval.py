class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        intervals.append(newInterval)
        for el in sorted(intervals, key=lambda x: x[0]):
            if result and el[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], el[1])
            else:
                result.append(el)
        return result
        