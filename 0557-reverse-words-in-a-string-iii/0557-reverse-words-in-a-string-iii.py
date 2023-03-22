class Solution:
    def reverseWords(self, s: str) -> str:
        s_array = s.split()
        result = []
        for word in s_array:
            result.append(word[::-1])
        return ' '.join(result)
