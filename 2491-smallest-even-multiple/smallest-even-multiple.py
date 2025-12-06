class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        x=n
        while n%2 !=0:
            x=n*2
            return x
        return x