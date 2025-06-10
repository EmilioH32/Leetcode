class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alpha_num = [char for char in s if char.isalnum()]
        left = 0
        right = len(alpha_num) - 1

        while left < right:
            if alpha_num[left] != alpha_num[right]:
                return False
            left += 1
            right -= 1
        return True