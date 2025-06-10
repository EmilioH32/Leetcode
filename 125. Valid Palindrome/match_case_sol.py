# current issue is edge cases with 3 length lists [1, a, 2], [a, b, a]
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alpha_num = [char for char in s if char.isalnum()]
        length = len(alpha_num)
        remainder = length % 2
        print(remainder, length, alpha_num)
        if not alpha_num:
            return True
        match remainder:
            case 0:
                for i in alpha_num[length // 2]:
                    if alpha_num.count(i) != 2:
                        return False
                    else:
                        return True
            case 1:
                for i in alpha_num[(length - 1) // 2]:
                    if alpha_num.index(i) == ((length - 1) // 2) or length != 3 or alpha_num.count(i) == 2:
                        return True
                    else:
                        return False