class Solution:
    @staticmethod
    def get_sum_of_squares_of_digits(num):
        res = 0
        while num > 0:
            res += (num % 10) ** 2
            num = num // 10
        return res
    
    def isHappy(self, n: int) -> bool:
        for _ in range(8):
            if n == 1:
                return True
            n = self.get_sum_of_squares_of_digits(n)
        return False
