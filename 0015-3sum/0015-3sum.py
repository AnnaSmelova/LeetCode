class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        neg, pos, zer = [], [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
            else:
                zer.append(num)
        N = set(neg)
        P = set(pos)

        if zer:
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))
        if len(zer) >= 3:
            res.add((0, 0, 0))
        for i in range(len(neg)):
            for j in range(i + 1, len(neg)):
                target = -1 * (neg[i] + neg[j])
                if target in P:
                    res.add(tuple(sorted([neg[i], neg[j], target])))
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                target = -1 * (pos[i] + pos[j])
                if target in N:
                    res.add(tuple(sorted([pos[i], pos[j], target])))
        return res
        