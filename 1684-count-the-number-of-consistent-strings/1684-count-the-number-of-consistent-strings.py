class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        cnt = 0
        for word in words:
            for letter in word:
                if letter not in allowed_set: 
                    cnt += 1
                    break
        return len(words) - cnt
