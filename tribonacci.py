#1137. n-th tribonaci number
def tribonacci(self, n: int) -> int:
  if n == 2: return 1
  if n == 1: return 1
  if n == 3: return 2
  step1 = 1
  step2 = 1
  step3 = 2
  curstep = 0
  for i in range(4,n+1):
    curstep = step1+step2+step3
    step1 = step2
    step2 = step3
    step3 = curstep
  return curstep
