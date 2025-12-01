class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        odd=1
        while num>0:
            num=num-odd
            odd+=2
        return num==0