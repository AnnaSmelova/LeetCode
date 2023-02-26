class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded)
        decoded = [0]*(n+1)
        decoded[0] = first
        for i in range(n):
            decoded[i+1] = (encoded[i] ^ decoded[i])
        return decoded
        