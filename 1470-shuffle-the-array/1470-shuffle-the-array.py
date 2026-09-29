class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = nums[:n]
        b = nums[n:]
        l = []
        for i in range(n):
            l.append(a[i])
            l.append(b[i])
        return l

        