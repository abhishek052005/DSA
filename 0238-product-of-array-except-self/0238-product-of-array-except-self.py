class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [0]* n

        left_product = 1
        for i in range(n):
            l[i] = left_product
            left_product *= nums[i]
  
        right_product = 1
        for i in range(n - 1, -1, -1):
            l[i] *= right_product
            right_product *= nums[i]


        return l


        