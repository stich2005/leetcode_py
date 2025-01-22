# 5. Longest Palindromic Substring
s = '|'+'|'.join(s)+'|' # символы для приведения к случаю четных палиндромов
        n = len(s)
        h = [0] * n
        C = R = 0      # центр и радиус или крайний правый палиндром
        besti, bestj = 0, 0     # центр и радиус самого длинного палиндрома
        for i in range(n):
            if i < C + R:         # если есть пересечение
                j = h[C-(i-C)]       # отражение
                if j < C + R - i:    # случай A
                    h[i] = j
                    continue
                elif j > C + R - i:  # случай B 
                    h[i] = C + R - i
                    continue
                else:                # case C 
                    pass
            else:                 # если нет пересечения
                j = 0
            while i-j > 0 and i+j<n-1 and s[i-j-1] == s[i+j+1]:
                j += 1
            h[i] = j
            if j > bestj:
                    besti, bestj = i, j
            if i + j > C + R:
                C, R = i, j
        return s[besti-bestj : besti+bestj+1].replace('|', '')
