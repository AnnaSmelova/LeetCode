class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt_2, cnt_5 = 0, 0
        for i in range(1, n + 1):
            num = i
            while num % 2 == 0:
                cnt_2 += 1
                num = num // 2
            while num % 5 == 0:
                cnt_5 += 1
                num = num // 5
        cnt = min(cnt_2, cnt_5)
        return cnt
        