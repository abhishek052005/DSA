class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        return len(nums) != len(numset)

        