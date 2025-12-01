class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,h=1,num
        while l<=h:
            mid=(l+h)//2
            if mid*mid == num:
                return True
            elif mid*mid <num:
                l=mid+1
            else:
                h=mid-1
        return False