#1572. Matrix diagonal sum
def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum = 0
        if n == 1: return mat[0][0]
        for i in range(n):
            sum += mat[i][i]
        for i in range(n):
            sum += mat[i][n-i-1]
        if n%2 != 0:
            sum -= mat[n//2][n//2]
        return sum
