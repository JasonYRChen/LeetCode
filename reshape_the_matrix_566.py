class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        def yield_element(mat):
            for row in mat:
                for element in row:
                    yield element


        width, height = len(mat[0]), len(mat)
        if (width * height // r) == c and not (width * height) % r:
            y = yield_element(mat)
            return [[next(y) for _ in range(c)] for _ in range(r)]
        return mat
