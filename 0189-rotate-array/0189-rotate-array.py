class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(k):
            s = nums[n-1]
            nums.insert(0,s)
            nums.pop(n)
        