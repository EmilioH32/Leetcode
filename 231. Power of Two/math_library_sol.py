import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        try:
            if 2 ** math.floor(math.log2(n)) != n:
                return False
            return True
        except:
            return False