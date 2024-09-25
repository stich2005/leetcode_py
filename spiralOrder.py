#54 Spiral Matrix
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n == 1: return matrix[0]
        m = len(matrix[0])
        out = []
        if m == 1:
            for k in range(n):
                out.append(matrix[k][0])
            return out
        i = 0
        j = 0
        while (n>0 and m>0):
            for k in range(m):
                out.append(matrix[i][k+j])
        #print(i, j+k, 'цикл1')
            if n-1 == 0: break
            for k in range(n-1):
                out.append(matrix[k+i+1][m+j-1])
        #print(k+i+1, m+j-1, 'цикл2')
            if m-1 == 0: break
            for k in range(m-1):
                out.append(matrix[n+i-1][m+j-2-k])
        #print(n+i-1,m+j-2-k , 'цикл3')
            for k in range(n-2):
                out.append(matrix[n-2+i-k][j])
        #print(n-k-2, j, 'цикл4')
            i += 1
            j += 1
            n -= 2
            m -= 2
        return out
