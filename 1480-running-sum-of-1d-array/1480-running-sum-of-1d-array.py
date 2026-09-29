class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        run =[0]*n
        run[0] = nums[0]
        for i in range(1,n):
            run[i]= run[i-1]+nums[i]
        return run
        