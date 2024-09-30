#43. Multiply strings
def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        ans = 0
        a = num1.split()
        b = num2.split()
        for i in a:
            for k in b:
                ans += int(i)*int(k)
        return str(ans)
