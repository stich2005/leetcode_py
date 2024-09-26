#1491. Average salary excluding the minimum and maximum salary
def average(self, salary: List[int]) -> float:
  iMin = min(salary)
    iMax = max(salary)
    salary.remove(iMin)
    salary.remove(iMax)
    iSum = sum(salary)
    return iSum/len(salary)
