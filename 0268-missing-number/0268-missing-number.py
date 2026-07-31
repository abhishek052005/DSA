class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        n = len(nums)
        for i in nums:
            sum += i
        tot = n*(n+1)/2
        return int(tot-sum)


        