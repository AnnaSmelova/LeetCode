class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        if len(time) == 1:
            return time[0] * totalTrips
        l, r = 1, min(time) * totalTrips
        while l < r:
            mid = (l + r) // 2
            total = 0
            for t in time:
                total += mid // t
            if total < totalTrips:
                l = mid + 1
            else:
                r = mid
        return l
