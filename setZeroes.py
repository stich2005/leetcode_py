#53. Set matrix zeroes
def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        n = len(matrix[0])
        indexes = []
        for i in range(row):
            if 0 in matrix[i]:
                indexes += [p for p, x in enumerate(matrix[i]) if x == 0]
                matrix[i][0] = 0
        for j in range(row):
            if matrix[j][0] == 0:
                for h in range(1,n):
                    matrix[j][h] = 0
        for f in range(len(indexes)):
            for t in range(row):
                matrix[t][indexes[f]] = 0
