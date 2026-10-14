class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        num = [i**2 for i in nums]
        num.sort()
        n = len(num)
        n1 = num[:n//2]
        n2 = num[n//2:]
        sum1 =0   
        sum2 =0   
        for i in n1:
            sum1 = sum1 + i
        for i in n2:
            sum2 = sum2 + i
        return sum2 - sum1

        