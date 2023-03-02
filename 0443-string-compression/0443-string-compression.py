class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            cnt = 1
            while (i + cnt < len(chars) and chars[i + cnt] == chars[i]):
                cnt += 1
            chars[res] = chars[i]
            res += 1
            if cnt > 1:
                cnt_str = str(cnt)
                chars[res:res+len(cnt_str)] = list(cnt_str)
                res += len(cnt_str)
            i += cnt
        return res
                




