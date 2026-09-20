class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for index, i in enumerate(s):
            a = ord(i.upper())-ord('A')+1
            b = 27-a
            c = b*(index+1)
            total += c
        return total
        