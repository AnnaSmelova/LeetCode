class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        allowed_set = set(allowed)
        for word in words:
            word_set = set(word)
            if len(word_set & allowed_set) == len(word_set):
                cnt += 1
        return cnt
