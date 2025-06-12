class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt = int(num ** .5)
        if sqrt * sqrt != num:
            return False
        else:
            return True