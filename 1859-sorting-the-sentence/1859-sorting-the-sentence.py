class Solution:
    def sortSentence(self, s: str) -> str:
        temp = s.split()
        temp.sort(key = lambda s:s[-1])
        for i in range(len(temp)):
            temp[i] = temp[i][:-1]
        return ' '.join(temp)
        