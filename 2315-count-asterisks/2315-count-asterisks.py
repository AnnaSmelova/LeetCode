class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt_bar = 0
        cnt_star = 0
        for i in s:
            if i == '|':
                cnt_bar += 1
                cnt_bar = cnt_bar % 2
            elif i == '*':
                if cnt_bar == 0:
                    cnt_star += 1
        return cnt_star
        