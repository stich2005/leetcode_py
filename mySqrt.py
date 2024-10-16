#69. Sqrt(x)
def mySqrt(self, x: int) -> int:
        low=0
        hight = x
        while low <= hight:
            mid = (low + hight) // 2
            if mid*mid <= x and (mid+1)*(mid+1)>x:
                return mid
            if mid*mid > x:
                hight = mid - 1
            else: low = mid + 1
