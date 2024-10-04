#70. Climbing tsears
def climbStairs(self, n: int) -> int:
        if n == 2: return 2
        if n == 1: return 1
        step1 = 1
        step2 = 2
        curstep = 0
        for i in range(3,n+1):
            curstep = step1+step2
            step1 = step2
            step2 = curstep
        return curstep
