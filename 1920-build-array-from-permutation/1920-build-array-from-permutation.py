class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        arr = []
        for i in range(len(nums)):
            x = nums[nums[i]]
            arr.append(x)
        return arr
        