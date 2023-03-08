class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return piles[0] // h if piles[0] % h == 0 else piles[0] // h + 1

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            time = 0
            for i in piles:
                if i <= mid:
                    time += 1
                else:
                    if i % mid == 0:
                        time += i // mid
                    else:
                        time += i // mid + 1
            if time > h:
                left = mid + 1
            else:
                right = mid

        return right
