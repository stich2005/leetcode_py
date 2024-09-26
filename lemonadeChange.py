#860. Lemonade change
def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        x5 = 0
        x10 = 0
        for i in bills:
            if i == 5:
                x5 += 1
            elif i == 10:
                x10 += 1
                if x5 != 0:
                    x5 -= 1
                else: return False
            else:
                if x10 > 0 and x5 >0:
                    x10 -=1
                    x5 -=1
                elif x5 > 2:
                    x5 -= 3
                else: return False
        return True
