class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum = 0
        prod = 1
        for i in str(n):
            sum += int(i)
            prod *= int(i)
        tot = sum + prod
        return n % tot== 0 if n != 0 else False
