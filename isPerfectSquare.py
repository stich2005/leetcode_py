#367 Valid perfect square
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        low=2
        hight = num
        while low <= hight:
            mid = (low + hight) // 2
            guess = mid*mid
            if guess == num:
                return True
            if guess > num:
                hight = mid - 1
            else: low = mid + 1
        return False
