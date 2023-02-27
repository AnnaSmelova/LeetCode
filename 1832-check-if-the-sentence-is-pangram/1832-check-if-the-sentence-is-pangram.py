class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sent = set(sentence)
        alphabet = set(string.ascii_lowercase)
        if sent == alphabet:
            return True
        return False
