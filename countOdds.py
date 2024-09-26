#1523. Count odd number in an interval range
def countOdds(self, low: int, high: int) -> int:
        count = (high - low)//2
        if (high - low)%2 != 0:
            count +=1
        if high%2 != 0 and low%2 !=0:
            count +=1
        return count
