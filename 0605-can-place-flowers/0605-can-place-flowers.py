class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        m = len(flowerbed)
        if n > m:
            return False
        for i in range(m):
            if flowerbed[i] == 0:
                if (i > 0 and flowerbed[i - 1] == 0) or (i == 0):
                    if (i < m - 1 and flowerbed[i + 1] == 0) or (i == m - 1):
                        flowerbed[i] = 1
                        n -= 1
                        if n == 0:
                            return True
        return False
