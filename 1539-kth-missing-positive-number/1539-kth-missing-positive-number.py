class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        full_arr_set = set(range(1, arr[-1] + k + 1))
        arr_set = set(arr)
        diff = sorted(list(full_arr_set - arr_set))
        return diff[k - 1]
