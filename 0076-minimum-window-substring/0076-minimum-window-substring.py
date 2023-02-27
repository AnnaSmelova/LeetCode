class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        miss  = len(set(t))
        l, r  = 0, 0
        wl, wr = -1, len(s)
        while True:
            if r < len(s) and miss > 0:
                freq[s[r]] -= 1
                if freq[s[r]] == 0: 
                    miss -= 1
                r += 1
            elif l < len(s) and miss <= 0:
                if r-l < wr-wl: 
                    wr, wl = r, l
                if freq[s[l]] == 0: 
                    miss += 1
                freq[s[l]] += 1
                l += 1   
            else:
                break
        return s[wl:wr] if wl >= 0 else ""
