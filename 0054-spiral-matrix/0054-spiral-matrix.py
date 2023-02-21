class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        elements = []
        while matrix:
            elements += matrix.pop(0) ## top
            elements += [row.pop() for row in matrix] ## right
            if not matrix or not matrix[0]: break
            elements += matrix.pop()[::-1] ## bottom
            elements += [row.pop(0) for row in matrix][::-1] ## left
            if not matrix or not matrix[0]: break
        return elements
